# Imports
from rest_framework import status
# from rest_framework_request import Request 
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Utils
from .utils.stack import Stack
from .utils.queue import Queue
from .utils.graph import Graph
import random
import json
import time
import pdb

# ENV
from decouple import config

# Models
from .models import Room
from .serializers import RoomSerializer

# Scripts
from .scripts.testScript import testScript
from .scripts.movement import movement
from .scripts.getStatus import getStatus

# Pre Installed
from django.shortcuts import render

# Create your views here.
# TEST SCRIPT
@api_view(['GET', ])
def Test_Script(request):
    result = testScript()
    return Response(result)
# - - - -

# == STATUS ==
## FUNCTION BASED VIEW
@api_view(['GET', ])
def STATUS(request):
    print(f'- - - status/ GET \n --body:{request.body}')

    TOKEN = config('TOKEN')
    print(TOKEN)

    header = {
        'Authorization': 'Token '+ TOKEN,
        'Content-Type': 'application/json'
    }
    print(header)
    
    if request.method == 'GET':
        data = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=header).json()

        print(f'THIS IS THE CURRENT STATUS {data}')
        # return Response(data)
        return data
    # try:
    #     pass

    #     # TODO: Convert ^^ to imported script
    #     # getStatus()
    # except:
    #     response = {'response': 'this is reponse'}
    #     return Response(response)
# - - - -

# == TRAVERSE ==
@api_view(['GET',])
def traverseMap(request):
    print(f'- - - traverse/ GET \n --body:{request.body}')
    welcome_message = f'PRAISE JESUS YOU BOUT TO GO SSSPLORINN!!'
    print(welcome_message)

    # Header
    TOKEN = config('TOKEN')
    header = {
        'Authorization': 'Token '+ TOKEN,
        'Content-Type': 'application/json'
    }
    # print(header)

    # Initialize Player 
    def initialization():
        startingRoom = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=header).json()

        return startingRoom
    
    def find_unused_exits(currentRoom_OBJECT, world_graph, backtrack=False):
        print(f' -*- You are trying to find a "?" in your graph')
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']])
        # print(currentRoom_OBJECT['exits'])

        if backtrack:
            print(currentRoom_OBJECT)
            # pdb.set_trace()

        result = []
        backtrack_result_unexplored = []
        backtrack_result_known = []
        avail_exits = world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']
        print(f'AVAIL EXITS: {avail_exits}')

        if backtrack:
            # print(f'AVAIL EXITS: {avail_exits}')
            # pdb.set_trace()
            pass


        for dir in avail_exits:
            if dir in avail_exits and avail_exits[dir] == "?":
                result.append(dir)

            # Backtrack Logic
                if backtrack:
                    backtrack_result_unexplored.append(dir)
            if dir in avail_exits and avail_exits[dir] is not None:
                backtrack_result_known.append(dir)

        # Return
        if backtrack:
            print(f'FILTERED EXITS: {backtrack_result_unexplored, backtrack_result_known}')
            return backtrack_result_unexplored, backtrack_result_known
        else:
            print(f'FILTERED EXITS: {result}')
            return result
    
    def randomChoice(filteredExits):
        chosen_direction = filteredExits[random.randint(0, len(filteredExits) - 1)]
        print(f'-*- CHOSEN DIRECTION: {chosen_direction}')
        
        return chosen_direction

    # Move Player
    def move(direction, currentRoom_OBJECT, world_graph, traversal_path, explored_rooms):
        opposite = {"n": "s", "e": "w", "s": "n", "w": "e"}
        print(f'-*- Attempting MOVEMENT: {direction} from {currentRoom_OBJECT}')
        
        # Make New Room
        newRoom_OBJECT = requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', 
            data=json.dumps({"direction": direction}),
            headers=header).json()
        print(newRoom_OBJECT)
        # pdb.set_trace()
        traversal_path.append((direction, newRoom_OBJECT['room_id']))
        print(traversal_path)

        ## Check
        # print(f'-*- New ROOM: {newRoom_OBJECT}')
        # print(f'-*- New TRAVERSAL PATH: {newRoom_OBJECT}')
        
        # - - - - 
        print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
        
        # Update Graph
        if newRoom_OBJECT['room_id'] not in world_graph.vertices:
            # Add Vertex
            world_graph.add_vertex(newRoom_OBJECT, world_graph)
            # Add Edges # only need one call to add_edge because it goes in both directions inside the function
            world_graph.add_edge(currentRoom_OBJECT['room_id'], direction, newRoom_OBJECT['room_id'])

        # print(f'-- AFTER MOVING --')
        # print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
        # - - - - 

        # Respect Cooldown -- from NEW ROOM object
        print(newRoom_OBJECT['cooldown'])
        time.sleep(newRoom_OBJECT['cooldown'])

        world_graph.print_graph()
        # pdb.set_trace()
        return newRoom_OBJECT, world_graph, traversal_path

    # First time you have been in this room
    def exploreRoom(currentRoom_OBJECT, uniqueTitles):
        # TITLE OF INTEREST 
        titles = ["Pirate Ry's", ]

        if currentRoom_OBJECT['title'] in titles:
            print('LOOK THIS SHUT UP')
            # pdb.set_trace()

        if currentRoom_OBJECT['title'] not in uniqueTitles:
            print(currentRoom_OBJECT['title'])
            uniqueTitles.append(currentRoom_OBJECT['title'])
            print(uniqueTitles)
            # pdb.set_trace()
            
        # - - - - 
        return 'continue_searching'

    def print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms, world_graph):
        print('\n\n')

        print(f'__ ALGO STATUS__\n ')
        print(f'-*- CURRENT ROOM: {currentRoom_OBJECT}')
        print(f'-*- EXPLORED ROOMS: {explored_rooms}')
        print(f'-*- TRAVERSAL PATH: {traversal_path}')
        # print(f'-*- GRAPH: {world_graph.print_graph()}')
        print('\n\n')
        # - - - -
        # pdb.set_trace()
    
    def print_BACKTRACK_status(BFS_QUEUE, BFS_PATHS, curr_BFS_room, current_vertex, world_graph):
            print('\n\n\n')

            print(f'  __MAIN BACKTRACK GOAL LOOP__ \n ')
            print(f'--CURRENT QUEUE: {BFS_QUEUE}')
            print(f'--CURRENT PATH: {BFS_PATHS}')
            world_graph.print_graph()
            print(f'CURRENT BFS ROOM: {curr_BFS_room}')
            print(f'CURRENT BFS VERTEX: {current_vertex}')
            # - - - -
            # pdb.set_trace()
            print('\n\n\n')

    def runBacktrack(currentRoom_OBJECT, world_graph):
        '''
        Think of this as a TOTALLY deparate operation with the benefit of having some map knowledge

        BFS on the GRAPH ... NOT actually moving character
        '''
        print(f'STARTING BACKTRACK -- inside backtrack')

        BFS_QUEUE = Queue()
        BFS_QUEUE_shortestPath = Queue()
        visitedRooms = set() # integers => room_id
        # - - - -

        # Start Queues
        BFS_QUEUE.enqueue(currentRoom_OBJECT)
        BFS_QUEUE_shortestPath.enqueue([currentRoom_OBJECT['room_id']])

        # print(BFS_QUEUE)
        print(BFS_QUEUE_shortestPath)
        # - - - - 
        # while BFS_QUEUE.size() > 0:
        while BFS_QUEUE_shortestPath.size() > 0:
            print(f'__MAIN BACKTRACK GOAL LOOP')

            # Get new item
            backtrackRoom_OBJECT = BFS_QUEUE.dequeue()
            backtrackPath = BFS_QUEUE_shortestPath.dequeue()
            current_vertex = world_graph.vertices[backtrackRoom_OBJECT['room_id']]
            visitedRooms.add(current_vertex['room_id'])
            print(f'-*- CURRENT BACKTRACK ROOM: {backtrackRoom_OBJECT}')
            print(f'-*- CURRENT BACKTRACK PATH: {backtrackPath}')
            print(f'-*- CURRENT VERTEX: {current_vertex}')
            # - - - - 

            # Filter Exits
            filtered_exits = find_unused_exits(current_vertex, world_graph, True)
            print(f'-*- FILTERED EXITS -- TEST of unexplored {filtered_exits[0]}')
            print(f'-*- FILTERED EXITS -- TEST of known {filtered_exits[1]}')
            # - - - - 
            # pdb.set_trace()

            
            print(len(filtered_exits))
            print(len(filtered_exits[0]))
            print(len(filtered_exits[1]))
            # pdb.set_trace()


            # WE FOUND IT
            if len(filtered_exits[0]) > 0:
                # print(f'WE FOUND IT.. RETURN THE PATH')
                # print(f'This is the path: {backtrackPath}')

                # # pdb.set_trace()
                # return backtrackPath
                pass 
            # We did not find it 
            else:   
                print(f'LOOK HERE FUCEKRS !#$%^&*^%$#$%^& 999 {filtered_exits[1]}')
                # Enqueu
                for direction in filtered_exits[1]:
                    print(current_vertex['exits'][direction])
                    newRoom = world_graph.vertices[
                        current_vertex['exits'][direction]
                    ] 
                    print(newRoom)
                    # pdb.set_trace()
                    print(visitedRooms)

                    
                    # Return OR Enqueue for next iteration
                    for exit in newRoom['exits']:
                        print(newRoom['exits'][exit])
                        if newRoom['exits'][exit] == "?":
                            print(f'WE FOUND IT -- here.. RETURN THE PATH')
                            backtrackPath.append(direction)
                            print(f'This is the path: {backtrackPath}')
                            # pdb.set_trace()                            
                            return backtrackPath

                    # pdb.set_trace()å
                    if newRoom['room_id'] in visitedRooms:
                        print('dont add this bitch ')
                    else: 
                        print('ADD THIS BITCH!!')
                        # Update Room Queue
                        BFS_QUEUE.enqueue(newRoom)

                        # Update Path
                        DUPLICATE_path = list(backtrackPath)
                        DUPLICATE_path.append(direction)
                        BFS_QUEUE_shortestPath.enqueue(DUPLICATE_path)
                    
                    print(BFS_QUEUE_shortestPath)

                    # pdb.set_trace()


                

                # pdb.set_trace()
                # pdb.set_trace()
                
            # - - - - 
            
            # pdb.set_trace()

    def addRoom_to_DB(room_OBJECT):
        print(room_OBJECT)
        # {
        #     'room_id': 239, 
        #     'title': 'A misty room', 
        #     'description': 'You are standing on grass and surrounded by a dense mist. You can barely make out the exits in any direction.', 
        #     'coordinates': '(62,50)', 
        #     'elevation': 0, 
        #     'terrain': 'NORMAL', 
        #     'players': [], 
        #     'items': ['tiny treasure', 
        #     'tiny treasure'], 
        #     'exits': ['n', 'w'], 
        #     'cooldown': 1.0, 
        #     'messages': []
        # }
        try:
            result = Room.objects.get(room_id=room_OBJECT['room_id'])
            print(f'DONT add another room')
        except:
            DB_room = Room(
                room_id=room_OBJECT['room_id'],
                title=room_OBJECT['title'],
                description=room_OBJECT['description'],
                coordinates=room_OBJECT['coordinates'],
                elevation=room_OBJECT['elevation'],
                terrain=room_OBJECT['terrain'],
                players=room_OBJECT['players'],
                items=room_OBJECT['items'],
                exits=room_OBJECT['exits'],
                cooldown=room_OBJECT['cooldown'],
                messages=room_OBJECT['messages'],
            )
            print(DB_room)
            DB_room.save()
            # pdb.set_trace()




    def runTraversal():
        # - A - SETUP
        world_graph = Graph()
        explored_rooms = set()
        DFS_STACK = Stack()
        traversal_path = []
        uniqueTitles = []
        # - - - - 

        # Clean out current DB
        # Delete Current Rooms
        Room.objects.all().delete()
        # - - - - 
        # pdb.set_trace()

        # - B - STEPS
        # Player Init
        startingRoom = initialization()
        
        traversal_path.append(startingRoom['room_id'])
        world_graph.add_vertex(startingRoom, world_graph)
        DFS_STACK.push(startingRoom)
        
        # Add Room Object to DB 
        print(f'STARTING ROOM: {startingRoom}')
        addRoom_to_DB(startingRoom)
        
        # Initiate Cooldown
        time.sleep(startingRoom['cooldown'])
        # - - - - 

        # __MAIN GOAL LOOP__
        '''
        When we get here the first time we have
        - Traversal path = starting_roo`m => this is going to be update to "currentRoom_OBJECT" for the rest of the function
        - NO room in explored_rooms
        - 1 vertex on graph
        - 1 room in DFS stack 
        '''
        while len(explored_rooms) < 500:
            print(f'  __MAIN GOAL LOOP__ \n ')
            # -- GET ITEM FROM STACK --
            currentRoom_OBJECT = DFS_STACK.pop()
            
            if currentRoom_OBJECT['room_id'] not in explored_rooms:
                # Add Room Object to DB 
                addRoom_to_DB(currentRoom_OBJECT)

            # -- TOP OF LOOP PRINT STATUS CHECK --
            print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
            # - - - -

            # -- New Room Loop // Check for special features // Take special actions -- 
            exploreRoom(currentRoom_OBJECT, uniqueTitles)
            # Add room to explored rooms
            explored_rooms.add(currentRoom_OBJECT['room_id'])
            # - - - -

            # -- Filter exits --
            unused_exits = find_unused_exits(currentRoom_OBJECT, world_graph)
            # print(f'FILTERED EXITS {unused_exits}')
            
        
            # -- Filtered exits Conditional -- 
            if len(unused_exits) > 0:
                # Choose random direction
                movementDirection = randomChoice(unused_exits)
                # - - - - 
                
                # Move in that direction
                movementResult = move(movementDirection, currentRoom_OBJECT, world_graph, traversal_path, explored_rooms)
                # Update Variables w/ Movement Result
                currentRoom_OBJECT = movementResult[0]
                world_graph = movementResult[1]
                traversal_path = movementResult[2]
                # - - - - 

                # print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
                
                # Update Stack
                DFS_STACK.push(currentRoom_OBJECT)
                
            else:
                print('START BACKTRACKING')
                print('\n\n\n')
                backtrack_RESULT = runBacktrack(currentRoom_OBJECT, world_graph)
                print(f'-*- THIS IS THE BACKTRACK RESULT {backtrack_RESULT}')
                # pdb.set_trace()
                

                # print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
                

                for step in backtrack_RESULT:
                    print(f'-- BACKTRACKING TO ROOM WITH UNUSED EXIT!! --')
                    print(step)
                    # pdb.set_trace()

                    movementResult = move(step, currentRoom_OBJECT, world_graph, traversal_path, explored_rooms)
                    
                    currentRoom_OBJECT = movementResult[0]
                    world_graph = movementResult[1]
                    traversal_path = movementResult[2]
                # - - - - 

                # Update Stack
                DFS_STACK.push(currentRoom_OBJECT)
                # - - - - 
                # pdb.set_trace()
        
    runTraversal()

    print(f' ----- THIS IS THE END ------ ')
    # pdb.set_trace()

# == ROOMS ==
## FUNCTION BASED VIEW
@api_view(['GET', ] )
def Rooms_View(request):
    try: 
        rooms = Room.objects.all()
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': # not really needed... but a good double check
        serializer = RoomSerializer(rooms, many=True) # look more into many=true flag
        return Response(serializer.data)

## CLASS BASED VIEW
class Rooms(APIView):

    def get(self, request):
        try: 
            rooms = Room.objects.all()
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomSerializer(rooms, many=True) # look more into many=true flag
    
        return Response(serializer.data)
    
    def post(self, request):
        pass
# - - - -
    
