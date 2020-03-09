# IMPORTS
import pdb 
import json

# SCRIPTS
from utils.make_node import make_node
from utils.get_graphData import get_graphData
from utils.pick_randomDirection import pick_randomDirection

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

    # Find vertex
    for entry in GOD_graph:
        print(entry)
        if entry['room_id'] == current_room['room_id']:
            GOD_vertex = entry
            break
    for entry in INSTANCE_graph:
        if entry['room_id'] == current_room['room_id']:
            INSTANCE_vertex = entry
            break
    # Debug
    if DEBUG_print:
        print(f'---DEBUG--- GOD_vertex {GOD_vertex}')
        print(f'---DEBUG--- INSTANCE_vertex {INSTANCE_vertex}')
    # - - - - 
    
    ''' Q: What exit should we choose? '''
    pick_result = pick_randomDirection(target, GOD_vertex, INSTANCE_vertex)
    
    if LIVE_print:
        print(f'-  🧭  🧭  🧭  - pick_result/\n{pick_result}')

    ''' Q: Can we break out of the DFS loop?? have we found our target? '''
    # Target Type = "?"
    if pick_result == False:
        print('🎉🎉 SUCCESS 🎉🎉')
        print('🎉🎉 DTF (search for "?") has found a room with an unused exit 🎉🎉')
    else:
        print('TIME TO MOVE')
        import pdb; pdb.set_trace()
        # Move


        # Recurse
        DFT(target, current_room, FILENAME__GOD_graph, FILENAME__INSTANCE_graph)






        