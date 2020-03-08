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
with open('GOD_graph.txt', 'w+') as json_file:
    try:
        data = json.load(json_file)
        GOD_graph = data
        for line in data:
            print(line)
        
        if LIVE_print:
            print(f'-  👼  👼  👼  - GODs got your back!')
            print(f'-  🗺  🗺  🗺  - Heres a map 🎅🏿/\n{GOD_graph}')

    except:
        GOD_graph = None
        if LIVE_print:
            print(f'-  😱  😱  😱  - GOD Graph is EMPTY!/\n{GOD_graph}')

### 3.1 -- Make INSTANCE graph
random_number = random.randint(0, 100000000000)
# new_file = open({[random_number].txt, 'w+'} as outfile):
# with open(random_number + '_instance', 'w+') as json_file:
FILENAME__INSTANCE_Graph = "%instance.txt" % random_number
with open(FILENAME__INSTANCE_Graph, 'w+') as json_file:
    try:
        data = json.load(json_file)
        INSTANCE_graph = data
        for line in data:
            print(line)
        
        if LIVE_print:
            print(f'-  🗺  🗺  🗺  - Heres your map/\n{INSTANCE_graph}')

    except:
        INSTANCE_graph = None
        if LIVE_print:
            print(f'-  😱  😱  😱  - Your map is EMPTY!/\n{INSTANCE_graph}')
''' END -- Q: What do i know?? 

    - GOD_graph
    - INSTANCE_graph
'''

''' CALL DFT '''
DFT(target, current_room, "GOD_graph.txt", FILENAME__INSTANCE_Graph)







