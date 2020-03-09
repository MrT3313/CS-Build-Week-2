# IMPORTS
import json
import pdb

# SCRIPTS
from .make_genericRoom import make_genericRoom

# PRINTING
DEBUG_print = True
LIVE_print = True

def make_node(current_room, FILENAME):
# def make_node(room_id, graph, FILENAME):
    '''
        generic node maker for graph -- aka INSTANCE_graph or GOD_graph

    '''
    # if not graph:
    #     return 'ERROR'
    # print('in make node')
    # - - - - 
    
    node_data = make_genericRoom(current_room)
    # # node_data = {
    # #     'room_id': current_room['room_id'],
    # #     "n" : '?',
    # #     "s" : '?',
    # #     "e" : '?',
    # #     "w" : '?',
    # # }
    # walls = [exit for exit in ['n','s','e','w',] if exit not in current_room['exits'] ]
    # for exit in walls:
    #     node_data[exit] = None

    # Print & Debug:
    if DEBUG_print:
        print(FILENAME)
    if LIVE_print:
        print(f'-  👷🏼‍♂️  👷🏼‍♂️  👷🏼‍♂️  - Making a node')
        print(f'-  🖋  🖋  🖋  - FILENAME/\n{FILENAME}')
        print(f'-  🏗  🏗  🏗  - node_data/\n{node_data}')
    # - - - - 

    # Get current data 
    read = json.load(open(FILENAME, 'r'))

    # make new array for data
    new_array = []
    new_array.append(node_data)
    for entry in read:
        print(entry)
        new_array.append(entry)
    print(new_array)
    
    # Overwrite file ==> NOW its a feature...
    
    with open(FILENAME, 'w+') as file_toUpdate: 
        json.dump(new_array, file_toUpdate, indent=2)

    # Return 
    return node_data