# IMPORTS
import pdb 
import json

# SCRIPTS
from utils.make_node import make_node
from utils.get_graphData import get_graphData
from utils.pick_randomDirection import pick_randomDirection
from utils.move import move

# PRINTING
LIVE_print = True
DEBUG_print = True

print(__name__)

def DFT(target, current_room, FILENAME__GOD_graph, FILENAME__INSTANCE_graph):
    '''
        Keyword arguments:
            target(str): what are we looking for?
            current_room (obj): players current room
            GOD_graph (obj): persistant data
            INSTANCE__graph (obj): NOT persistant data
    '''
    if LIVE_print:
        print(f'-  🏡  🏡  🏡  - current_room/\n{current_room}')

    ''' Q: What are my exits?? '''
    if DEBUG_print:
        print(f'---DEBUG--- target/\n{target}')
        print(f'---DEBUG--- current_room/\n{current_room}')
        print(f'---DEBUG--- FILENAME__GOD_graph/\n{FILENAME__GOD_graph}')
        print(f'---DEBUG--- FILENAME__INSTANCE_graph/\n{FILENAME__INSTANCE_graph}')

    room_id = current_room['room_id']
    
    ''' Q: What do our graphs have '''
    graphData_RESULT = get_graphData(current_room, FILENAME__INSTANCE_graph)

    GOD_graph = graphData_RESULT[0]
    INSTANCE_graph = graphData_RESULT[1]

    if LIVE_print:
        print(f'First attempt')
        print(f'-  👼  👼  👼  - FILE NAME for: GOD_graph/\n{GOD_graph}')
        print(f'-  🧠  🧠  🧠  - FILE NAME for: INSTANCE__graph/\n{INSTANCE_graph}')
    # - - - - 

    # TODO: move these somewhere else...
    GOD_vertex = None
    INSTANCE_vertex = None
    for entry in GOD_graph:
        print(entry)
        if entry['room_id'] == current_room['room_id']:
            GOD_vertex = entry
            break
    if GOD_vertex == None:
        # We need to make a new vertex on the GOD_graph!
        print(FILENAME__GOD_graph)
        GOD_vertex = make_node(current_room, FILENAME__GOD_graph)

    for entry in INSTANCE_graph:
        if entry['room_id'] == current_room['room_id']:
            INSTANCE_vertex = entry
            break
    if INSTANCE_vertex == None:
        # We need to make a new vertex on the GOD_graph!
        print(FILENAME__INSTANCE_graph)
        INSTANCE_vertex = make_node(current_room, FILENAME__INSTANCE_graph)
    
    # Debug
    if DEBUG_print:
        print(f'---DEBUG--- GOD_vertex {GOD_vertex}')
        print(f'---DEBUG--- INSTANCE_vertex {INSTANCE_vertex}')
    # if INSTANCE_vertex == None or GOD_vertex == None:
    #     print('STOPPPPppp')
    #     pdb.set_trace()
    # - - - - ≈
    
    ''' Q: What exit should we choose? '''
    pick_result = pick_randomDirection(target, GOD_vertex, INSTANCE_vertex)
    
    if LIVE_print:
        print(f'-  🧭  🧭  🧭  - pick_result/\n{pick_result}')

    ''' Q: Can we break out of the DFS loop?? have we found our target? '''
    # Target Type = "?"
    if pick_result == False:
        print('🎉🎉 SUCCESS 🎉🎉')
        print('🎉🎉 DTF (search for "?") has found a room with an unused exit 🎉🎉')

        pdb.set_trace()
    else:
        print('TIME TO MOVE')
        
        # Move
        movement_result = move(pick_result, current_room)
        current_room = movement_result
        print('NEW CURRENT ROOM')
        print(current_room)
        
        # Recurse
        ## current_room IS movement_result for the next round
        ## filename & target dont change
        DFT(target, movement_result, FILENAME__GOD_graph, FILENAME__INSTANCE_graph)


        