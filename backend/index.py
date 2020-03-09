''' RUN THIS FILE EVERY TIME '''
''' RUN THIS FILE EVERY TIME '''
''' RUN THIS FILE EVERY TIME '''
# IMPORTS
import os
import random
import pdb
import json

# SCRIPTS
from utils.init_player import initialization
from scripts.DFT import DFT
from utils.make_genericRoom import make_genericRoom

from utils.random_functions import PRINT_python_project_structure

# UTILS
from utils.stack import Stack
from utils.graph import Graph

# PRINTING
LIVE_print = True
DEBUG_print = False

'''Q: What is my project file structure??'''
# FILE STRUCTURE
starting_path = os.getcwd()
if DEBUG_print:
    print(f'---DEBUG--- starting_path/\n{starting_path}')
PRINT_python_project_structure(starting_path)

'''Q: Where am I?? '''
## Step 1: Initialize Player
current_room = initialization()

if LIVE_print:
    print(f'-  🏡  🏡  🏡  - current_room/\n{current_room}')

''' Q: What is my current target?? '''
## Step 2: Assign target
target = '?'

''' Q: What do i know?? '''
## Step 3: Get Graph
### 3.2 -- Get GOD graph
#### Does graph exits

# VERSION 2


# Make Initial Vertex
graph_vertex = make_genericRoom(current_room)
print(graph_vertex)
data_prep = [graph_vertex,]
print(data_prep)

# - - - - 
# Update graphs
## GOD_graph
with open('GOD_graph.json', 'w+') as GOD_file:
    print(type(GOD_file))
    try: 
        GOD_data = json.load(GOD_file)
        print('we FOUND data')
    except:
        # json.dump(graph_vertex, GOD_file, indent=2)
        json.dump(data_prep, GOD_file, indent=2)
        
    finally: 
        if LIVE_print:
            print(f'-  🚧  🚧  🚧  - Created initial node on GOD_graph')
            # pdb.set_trace()
# - - - - 
## INSTANCE_graph
random_number = random.randint(0, 100000000000)
FILENAME__INSTANCE_Graph = f'{random_number}_instance.json'

with open(FILENAME__INSTANCE_Graph, 'w+') as INSTANCE_graph:
    try:
        INSTANCE_data = json.load(INSTANCE_graph)
        print(INSTANCE_data)
    except:
        # json.dump(graph_vertex, INSTANCE_graph)
        json.dump(data_prep, INSTANCE_graph, indent=2)
    finally:
        if LIVE_print:
            print(f'-  🚧  🚧  🚧  - Created initial node on INSTANCE_graph')
            # pdb.set_trace()
''' END -- Q: What do i know?? 
    - GOD_graph
    - INSTANCE_graph
'''

''' CALL DFT '''
DFT(target, current_room, "GOD_graph.json", FILENAME__INSTANCE_Graph)







