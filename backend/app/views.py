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
# from .scripts.movement import movement
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
    TOKEN = config('TOKEN')

    header = {
        'Authorization': 'Token '+ TOKEN,
        'Content-Type': 'application/json'
    }
    
    if request.method == 'GET':
        # Get Data
        data = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', 
            headers=header
        ).json()
        # - - - - 

        print(f'THIS IS THE CURRENT STATUS {data}')
        
        # Return
        return data
# - - - -

# == TRAVERSE ==
@api_view(['GET',])
def traverseMap(request):
    welcome_message = f'PRAISE JESUS YOU BOUT TO GO SSSPLORINN!!'
    print(f'\n\n{welcome_message}\n\n')

    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    ##                                  ## ##
    ##                CONFIG            ## ##
    ##                                  ## ## 
    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    # Header
    TOKEN = config('TOKEN')
    header = {
        'Authorization': 'Token '+ TOKEN,
        'Content-Type': 'application/json'
    }
    # - - - - 

    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    ##                                  ## ##
    ##           HELPER FUNCTIONS       ## ##
    ##                                  ## ## 
    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    def errorCheck(response_result, known_errors=[], known_messages=[]):
        result = False
        print(response_result)

        for message in response_result['messages']:
            if message not in known_messages:
                print(f'YOU FOUND A NEW MESSAGE')
                known_messages.append(message)

        for error in response_result['errors']:
            if error not in known_errors:
                known_errors.append(error)

        return result, known_errors, known_messages


    def make_request(reqType, baseURL, slug='', header={}, data={}):
        print(f'-- TRYING TO MAKE REQUEST --')
        print(f'{reqType} -- {baseURL}{slug}/ -- {data}')
        if reqType == 'get' or reqType == 'Get' or reqType == 'GET':
            response_data = requests.get(baseURL + slug + '/',
                data=json.dumps(data),
                headers=header
            ).json()
        # - - - -

        if reqType == 'post' or reqType == 'Post' or reqType == 'POST':
            response_data = requests.post(baseURL + slug,
                data=json.dumps(data),
                headers=header
            ).json()
        # - - - -
        # print(f'-*- MAKE REQUEST -- RESPONSE DATA/\n {response_data}')

        # COOLDOWN
        print(response_data)
        print(response_data['cooldown'])
        time.sleep(response_data['cooldown'])
        # - - - - 

        # Error Check 
        errorCheck_RESULT = errorCheck(response_data)
        main_errorCheck_RESULT = errorCheck_RESULT[0]
        known_error_messages = errorCheck_RESULT[1]
        known_messages = errorCheck_RESULT[2]
        # - - - - 

        return response_data


    def addRoom_to_DB(room_OBJECT):
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
            DB_room.save()
            # 


    def randomChoice(filteredExits):
        chosen_direction = filteredExits[random.randint(0, len(filteredExits) - 1)]
        print(f'-*- CHOSEN DIRECTION/\n {chosen_direction}')
        
        return chosen_direction


    def wiseExplorer_check(world_graph, currentRoom_OBJECT, direction):
        print(f'INSIDE WISE EXPLORER: ')
        print(f'DIRECTION: {direction}')
        # print(world_graph.vertices)
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']])
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']]['exits'])
        print(world_graph.vertices[currentRoom_OBJECT['room_id']]['exits'][direction])
        # - - - - 
    
        # what does the NEXT node on the GRAPH look like ??
        direction_result = world_graph.vertices[currentRoom_OBJECT['room_id']]['exits'][direction]

        '''
        Options: # , None , "?"
            If you get a # -- int back then you KNOW where your going 
        '''
        if isinstance(direction_result, int):
            return direction_result
        else:
            return False


    def item_interaction(item, type ='take'):
        slug = type + '/'
        print(slug)
        JSON_DUMPS_obj = {"name": item}
        # - - - - 

        # Request
        result = requests.post(f'https://lambda-treasure-hunt.herokuapp.com/api/adv/{slug}',
            data=json.dumps(JSON_DUMPS_obj),
            headers=header,
        ).json()

        # Respect Cooldown -- from NEW ROOM object
        print(result['cooldown'])
        time.sleep(result['cooldown'])
        # - - - - 

        return result



        # Get current status
        playerStatus = getStatus()
        print(playerStatus)
        # - - - - 

        # Examine item or player
        print(f'JSON DUMPS : {JSON_DUMPS_obj}')
        result = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
            data=json.dumps(JSON_DUMPS_obj),
            headers=header,
        ).json()
        print(result)

        # Respect Cooldown -- from NEW ROOM object
        print(result['cooldown'])
        time.sleep(result['cooldown'])
        # - - - - 

        # Pick up treasure
        print(playerStatus['encumbrance'])
        print(result['weight'])
        print(playerStatus['strength'])

        # if result['name'] == 'tiny treasure' or result['name'] == 'small treasure' and playerStatus['encumbrance'] + result['weight'] < playerStatus['strength']:
        if playerStatus['encumbrance'] + result['weight'] < playerStatus['strength']:

            print(f'PICK IT UP')
            
            interaction_RESULT = item_interaction(result['name'])
            print(interaction_RESULT)
        # - - - - 

        # Get current status
        playerStatus = getStatus()
        print(playerStatus)
        # - - - - 
        if 'Heavily Encumbered: +100% CD' in result['messages']:
            print(playerStatus)
            

        # - - - - 

        return result


    def getStatus():
        result = make_request(
            'POST', 'https://lambda-treasure-hunt.herokuapp.com/api/adv/', 'status', 
            header
            # No Data
        )

        # - - - - 
        print(f'status/ \n {result}')
        
        return result


    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    ##                                  ## ##
    ##         TRAVERSAL FUNCTIONS      ## ##
    ##                                  ## ## 
    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    ## TRAVERSAL HELP
    def initialization():
        startingRoom = make_request(
            'GET', 
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/', 'init', 
            header 
            #  no data
        )
        # - - - - 
        print(f'STARTING ROOM: {startingRoom}')
        
        # COOLDOWN
        print(startingRoom['cooldown'])
        time.sleep(startingRoom['cooldown'])

        # Return
        return startingRoom


    def exploreRoom(currentRoom_OBJECT, known_titles=[], known_items=[]):
        '''
        Whenever we enter a new room we want to explore it and update 
        our character in accordance with our current goal
        '''
        if currentRoom_OBJECT['title'] not in known_titles:
            known_titles.append(currentRoom_OBJECT['title'])
        # - - - - 

        if currentRoom_OBJECT['items'] not in known_items:
            known_items.append(currentRoom_OBJECT['items'])
        # - - - - 


        # SPECIFIC ROOM ACTIONS
        if currentRoom_OBJECT['title'] == "Pirate Ry's":
            pass

        if currentRoom_OBJECT['title'] == "Shop":
            pass
        
        if currentRoom_OBJECT['title'] == "Fully Shrine":
            pass

        # - - - - 

        # Look at all items
        list_of_items = currentRoom_OBJECT['items']
        if len(list_of_items) > 0: 
            for item in list_of_items:
                print(item)
                examine_results = examine(item=item)
                print(f'EXAMIN RESULT/\n {examine_results}')
                
                # Get Status
                current_status = getStatus()

                # Check Inventory
                if current_status['encumbrance'] + examine_results['weight'] < current_status['strength']:
                    print(f'PICK IT UP!')
                    item_interaction(item)
        # - - - - 

        # Return
        return known_titles


    def find_unused_exits(currentRoom_OBJECT, world_graph, backtrack=False):
        # Data Check
        # print(world_graph.vertices[currentRoom_OBJECT['room_id']])
        # print(currentRoom_OBJECT['exits'])
        # - - - - 

        # Setup
        result = []
        backtrack_result_unexplored = []
        backtrack_result_known = []
        avail_exits = world_graph.vertices[currentRoom_OBJECT['room_id']]['exits']
        print(f'AVAIL EXITS: {avail_exits}')
        # - - - - 

        # Loop through available exits
        for dir in avail_exits:
            # Find and append all "?" dir 
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
    
    
    def move(direction, currentRoom_OBJECT, world_graph, traversal_path, explored_rooms):
        print(f'-*- Attempting MOVEMENT/\n {direction} from {currentRoom_OBJECT}')
        
        # WISE EXPLORER CHECK
        wiseExplorer_RESULT = wiseExplorer_check(world_graph, currentRoom_OBJECT, direction)
        print(f'-*- WISE EXPLORER CHECK/\n {wiseExplorer_RESULT}')

        # Set request data
        if wiseExplorer_RESULT is False:
            JSON_DUMPS_obj = {
                "direction": direction,
            }
        else:
            JSON_DUMPS_obj = {
                "direction": direction,
                "next_room_id": str(wiseExplorer_RESULT)
            }
        # - - - - 

        # Make New Room
        newRoom_OBJECT = make_request(
            'POST',
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/', 'move', 
            header, 
            JSON_DUMPS_obj
        )

        traversal_path.append((direction, newRoom_OBJECT['room_id']))
        print(f'-*- TRAVERSAL PATH/\n {traversal_path}')
        # - - - - 
        
        # Update Graph
        if newRoom_OBJECT['room_id'] not in world_graph.vertices:
            # Add Vertex
            world_graph.add_vertex(newRoom_OBJECT, world_graph)
            # Add Edges # only need one call to add_edge because it goes in both directions inside the function
            world_graph.add_edge(currentRoom_OBJECT['room_id'], direction, newRoom_OBJECT['room_id'])
        # - - - - 

        # Respect Cooldown -- from NEW ROOM object
        print(newRoom_OBJECT['cooldown'])
        time.sleep(newRoom_OBJECT['cooldown'])
        # - - - - 

        # Return
        return newRoom_OBJECT, world_graph, traversal_path


    def runBacktrack(currentRoom_OBJECT, world_graph):
        '''
        Think of this as a TOTALLY deparate operation with the benefit of having some map knowledge

        BFS on the GRAPH ... NOT actually moving character
        '''
        print(f'STARTING BACKTRACK -- inside backtrack')

        # Setup
        BFS_QUEUE = Queue()
        BFS_QUEUE_shortestPath = Queue()
        visitedRooms = set() # integers => room_id
        # - - - -

        # Initialize
        BFS_QUEUE.enqueue(currentRoom_OBJECT)
        BFS_QUEUE_shortestPath.enqueue([currentRoom_OBJECT['room_id']])

        # - - - - 
        # while BFS_QUEUE.size() > 0:
        while BFS_QUEUE_shortestPath.size() > 0:
            print(f'-*- MAIN BACKTRACK GOAL LOOP/\n')

            # Explore Room
            

            # Get new item
            backtrackRoom_OBJECT = BFS_QUEUE.dequeue()
            backtrackPath = BFS_QUEUE_shortestPath.dequeue()
            current_vertex = world_graph.vertices[backtrackRoom_OBJECT['room_id']]
            visitedRooms.add(current_vertex['room_id'])
            # print(f'-*- CURRENT BACKTRACK ROOM: {backtrackRoom_OBJECT}')
            print(f'-*- CURRENT BACKTRACK PATH/\n {backtrackPath}')
            print(f'-*- CURRENT VERTEX/\n {current_vertex}')
            # - - - - 

            # Filter Exits
            filtered_exits = find_unused_exits(current_vertex, world_graph, True)
            print(f'-*- FILTERED EXITS -- TEST of unexplored/\n {filtered_exits[0]}')
            print(f'-*- FILTERED EXITS -- TEST of known/\n {filtered_exits[1]}')
            # - - - - 
            
            # Enqueu
            for direction in filtered_exits[1]:
                # print(current_vertex['exits'][direction])
                newRoom = world_graph.vertices[
                    current_vertex['exits'][direction]
                ] 

                
                # Return OR Enqueue for next iteration
                for exit in newRoom['exits']:
                    print(newRoom['exits'][exit])

                    if newRoom['exits'][exit] == "?":
                        backtrackPath.append(direction)
                        print(f'WE FOUND IT -- here.. RETURN THE PATH/\n {backtrackPath}')
                                                 
                        return backtrackPath

                
                if newRoom['room_id'] not in visitedRooms:
                    # Update Room Queue
                    BFS_QUEUE.enqueue(newRoom)

                    # Update Path
                    DUPLICATE_path = list(backtrackPath)
                    DUPLICATE_path.append(direction)
                    BFS_QUEUE_shortestPath.enqueue(DUPLICATE_path)
                
                print(BFS_QUEUE_shortestPath)    


    def examine(item=None, player=None):
        # Define Data Headers
        if item is not None: 
            JSON_DUMPS_obj = {'name': item}

        if player is not None:
            JSON_DUMPS_obj = { 'name': player}

        else:
            prioritize = True
            if prioritize:
                JSON_DUMPS_obj = {'name': item}
            else:
                print('ERROR in EXAMINE')
                exit()
        # - - - - 
        # Examine item
        request_response = make_request(
            'POST', 
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/', slug='examine', 
            header=header, 
            data=JSON_DUMPS_obj
        )
        # - - - - 

        # Return
        return request_response

        

    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    ##                                  ## ##
    ##          START THE TRAVERSAL     ## ##
    ##                                  ## ## 
    ## ## -- -- ## ## -- -- ## ## -- -- ## ##
    def runTraversal():
        # - A - SETUP
        world_graph = Graph()
        explored_rooms = set()
        DFS_STACK = Stack()
        traversal_path = []
        uniqueTitles = []
        # - - - - 

        # Clean out current DB => Delete Current Rooms
        ''' TODO: 
            Change to check for room and only update iff needed
        '''
        # Room.objects.all().delete()
        # - - - - 

        # - B - STEPS
        # Player Init
        startingRoom = initialization()
        # - - - - 

        # Make Updates
        traversal_path.append(startingRoom['room_id'])
        world_graph.add_vertex(startingRoom, world_graph)
        DFS_STACK.push(startingRoom)
        # Add Room Object to DB 
        addRoom_to_DB(startingRoom)
        # - - - -
        
        ##  --  ##  --  ##  --  ## 
        ##                      ##
        ##  __MAIN GOAL LOOP__  ##
        ##                      ##
        ## --  ##  --  ##  --   ## 
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
            print(f'-*- CURRENT ROOM/\n{currentRoom_OBJECT}')
            # Add Room Object to DB 
            if currentRoom_OBJECT['room_id'] not in explored_rooms:
                addRoom_to_DB(currentRoom_OBJECT)
            # - - - - 

            # Explore room
            known_titles = exploreRoom(currentRoom_OBJECT)
            explored_rooms.add(currentRoom_OBJECT['room_id'])
            # - - - -
            
            # -- Filter exits --
            unused_exits = find_unused_exits(currentRoom_OBJECT, world_graph)
            # print(f'FILTERED EXITS {unused_exits}')

            # -- LOOP THROUGH ALL EXITS -- 
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
                
                # Update Stack
                DFS_STACK.push(currentRoom_OBJECT)

                ## LOOP STOP
                ## LOOP STOP
                # pdb.set_trace()        
                ## LOOP STOP
                ## LOOP STOP
            else:
                # BACKTRACK
                print('-*- START BACKTRACKING/\n')
                backtrack_RESULT = runBacktrack(currentRoom_OBJECT, world_graph)
                print(f'-*- THIS IS THE BACKTRACK RESULT/\n {backtrack_RESULT}')
                # - - - - 
                # pdb.set_trace()
                
                # Follow shortest path to room with unexplored exit
                for step in backtrack_RESULT[1:]:
                    print(f'-*- FOLLOW SHORTEST PATH')
                    print(step)

                    # Move in that direction
                    movementResult = move(step, currentRoom_OBJECT, world_graph, traversal_path, explored_rooms)
                    
                    currentRoom_OBJECT = movementResult[0]
                    world_graph = movementResult[1]
                    traversal_path = movementResult[2]
                # - - - - 

                # Update Stack
                DFS_STACK.push(currentRoom_OBJECT)
                # - - - - 
        
    runTraversal()

    print(f' ----- THIS IS THE END ------ ')









    #  ======== ======== ======== ======== ======== ======== ======== #
    #  ======== ======== ======== ======== ======== ======== ======== #
    #  ======== ======== ======== ======== ======== ======== ======== #
    #  ======== ======== ======== ======== ======== ======== ======== #


    ## HELPER


    def print_BACKTRACK_status(BFS_QUEUE, BFS_PATHS, curr_BFS_room, current_vertex, world_graph):
            print('\n\n\n')

            print(f'  __MAIN BACKTRACK GOAL LOOP__ \n ')
            print(f'--CURRENT QUEUE: {BFS_QUEUE}')
            print(f'--CURRENT PATH: {BFS_PATHS}')
            world_graph.print_graph()
            print(f'CURRENT BFS ROOM: {curr_BFS_room}')
            print(f'CURRENT BFS VERTEX: {current_vertex}')
            # - - - -
            # 
            print('\n\n\n')

    def print_ALGO_status(traversal_path, currentRoom_OBJECT, explored_rooms, world_graph):
        print('\n\n')

        print(f'__ ALGO STATUS__\n ')
        # print(f'-*- CURRENT ROOM: {currentRoom_OBJECT}')
        print(f'-*- EXPLORED ROOMS: {explored_rooms}')
        print(f'-*- TRAVERSAL PATH: {traversal_path}')
        getStatus()
        # print(f'-*- GRAPH: {world_graph.print_graph()}')
        print('\n\n')
        # - - - -
        # 
    

    # - - - - 
    



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
    
