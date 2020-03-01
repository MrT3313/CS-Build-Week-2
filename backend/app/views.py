# Imports
from rest_framework import status
# from rest_framework_request import Request 
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Utils
from .utils.stack import Stack
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
    
    def find_unused_exits(currentRoom_OBJECT, world_graph):
        print(f' -*- You are trying to find a "?" in your graph')
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']])
        # print(currentRoom_OBJECT['exits'])

        result = []
        avail_exits = world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']

        for dir in avail_exits:
            if dir in avail_exits and avail_exits[dir] == "?":
                result.append(dir)

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

        print(f'-- AFTER MOVING --')
        print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
        # - - - - 

        # Respect Cooldown -- from NEW ROOM object
        print(newRoom_OBJECT['cooldown'])
        time.sleep(newRoom_OBJECT['cooldown'])


        # # set currentRoom_OBJECT direction from ? to NUMBER
        # print(world_graph.vertices)
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']])
        # print(world_graph.vertices[newRoom_OBJECT['room_id']])

        # if direction == 'n':
        #     print(f'-*- UPDATE FOR n')
        #     # print(world_graph.vertices[currentRoom_OBJECT['room_id']]['n_to'])
        #     # print(currentRoom_OBJECT['room_id'])
        #     # print(newRoom_OBJECT['room_id'])

        #     world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']['n'] = newRoom_OBJECT['room_id']
        #     world_graph.vertices[newRoom_OBJECT['room_id']]['exits']['s'] = currentRoom_OBJECT['room_id']
        #     # pass
        # if direction == 's':
        #     print(f'-*- UPDATE FOR s')
        #     print(world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']['s'])
        
        #     # print(currentRoom_OBJECT['room_id'])
        #     # print(newRoom_OBJECT['room_id'])
            
        #     world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']['s'] = newRoom_OBJECT['room_id']
        #     world_graph.vertices[newRoom_OBJECT['room_id']]['exits']['n'] = currentRoom_OBJECT['room_id']
        #     # pass
        # if direction == 'e':
        #     print(f'-*- UPDATE FOR e')
        #     # print(world_graph.vertices[currentRoom_OBJECT['room_id']]['e_to'])
        #     # print(currentRoom_OBJECT['room_id'])
        #     # print(newRoom_OBJECT['room_id'])

        #     world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']['e'] = newRoom_OBJECT['room_id']
        #     world_graph.vertices[newRoom_OBJECT['room_id']]['exits']['w'] = currentRoom_OBJECT['room_id']
        #     # pass
        # if direction == 'w':
        #     print(f'-*- UPDATE FOR w')
        #     # print(world_graph.vertices[currentRoom_OBJECT['room_id']]['w_to'])
        #     # print(currentRoom_OBJECT['room_id'])
        #     # print(newRoom_OBJECT['room_id'])

        #     world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']['w'] = newRoom_OBJECT['room_id']
        #     world_graph.vertices[newRoom_OBJECT['room_id']]['exits']['e'] = currentRoom_OBJECT['room_id']
        #     # pass
        
        world_graph.print_graph()
        # pdb.set_trace()
        return newRoom_OBJECT, world_graph, traversal_path

    # First time you have been in this room
    def exploreRoom(currentRoom_OBJECT):
        # TITLE OF INTEREST 
        titles = ["Pirate Ry's", ]

        if currentRoom_OBJECT['title'] in titles:
            print('LOOK THIS SHUT UP')
            pdb.set_trace()
            
        # - - - - 
        return 'continue_searching'

    def print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms, world_graph):
        print('\n\n\n')

        print(f'__ ALGO STATUS__\n ')
        print(f'-*- TRAVERSAL PATH: {traversal_path}')
        print(f'-*- CURRENT ROOM: {currentRoom_OBJECT}')
        print(f'-*- EXPLORED ROOMS: {explored_rooms}')
        print(f'-*- GRAPH: {world_graph.print_graph()}')
        print('\n\n\n')
        # - - - -
        # pdb.set_trace()

    def runTraversal():
        # - A - SETUP
        world_graph = Graph()
        explored_rooms = set()
        DFS_STACK = Stack()
        traversal_path = []
        # - - - - 

        # - B - STEPS
        # Player Init
        startingRoom = initialization()
        
        traversal_path.append(startingRoom['room_id'])
        world_graph.add_vertex(startingRoom, world_graph)
        DFS_STACK.push(startingRoom)
        
        # Initiate Cooldown
        time.sleep(startingRoom['cooldown'])
        # - - - - 

        # __MAIN GOAL LOOP__
        '''
        When we get here the first time we have
        - Traversal path = starting_room => this is going to be update to "currentRoom_OBJECT" for the rest of the function
        - NO room in explored_rooms
        - 1 vertex on graph
        - 1 room in DFS stack 
        '''
        while len(explored_rooms) < 500:
            print(f'  __MAIN GOAL LOOP__ \n ')
            # -- GET ITEM FROM STACK --
            currentRoom_OBJECT = DFS_STACK.pop()

            # -- TOP OF LOOP PRINT STATUS CHECK --
            print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
            # - - - -

            # -- New Room Loop // Check for special features // Take special actions -- 
            exploreRoom(currentRoom_OBJECT)
            # Add room to explored rooms
            explored_rooms.add(currentRoom_OBJECT['room_id'])
            # - - - -
            print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)


            # -- Filter exits --
            unused_exits = find_unused_exits(currentRoom_OBJECT, world_graph)
            print(f'FILTERED EXITS {unused_exits}')
            
        
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

                print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms , world_graph)
                
                # Update Stack
                DFS_STACK.push(currentRoom_OBJECT)
                
            else:
                print('START BACKTRACKING')
                pdb.set_trace()

            # - - - -

        
    runTraversal()

    print(f' ----- THIS IS THE END ------ ')
    pdb.set_trace()

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
    
