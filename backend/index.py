''' RUN THIS FILE EVERY TIME '''
''' RUN THIS FILE EVERY TIME '''
''' RUN THIS FILE EVERY TIME '''
# IMPORTS
import os

# SCRIPTS
# from ..utils.init_player import initialization
from utils.init_player import initialization

## random scripts
# from ..utils.random_functions import PRINT_python_project_structure
from utils.random_functions import PRINT_python_project_structure

# PRINTING
LIVE_print = True
DEBUG_print = False

# FILE STRUCTURE
starting_path = os.getcwd()
if DEBUG_print:
    print(f'---DEBUG--- starting_path/\n{starting_path}')
PRINT_python_project_structure(starting_path)

## Step 1: Initialize Player
current_room = initialization()

if LIVE_print:
    print(f'-  🏡  🏡  🏡  - current_room/\n{current_room}')
