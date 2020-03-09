# IMPORTS
import random

# PRINT
LIVE_print = True
DEBUG_print = True

# __ MAIN FUNCTION __
def pick_randomDirection(target, GOD_vertex, INSTANCE_vertex):
    # Check each direction
    for dir in ['n','s','e','w']:
        print(GOD_vertex['exits'][dir])
        print(INSTANCE_vertex['exits'][dir])

        if GOD_vertex['exits'][dir] != INSTANCE_vertex['exits'][dir]:
            print('SOMETHING IS OUT OF WACK')
        else:
            used_graph_vertex = GOD_vertex

    # Update exit arrays
    if DEBUG_print:
        print(f'---DEBUG--- used_graph_vertex/\n{used_graph_vertex}')
    
    known_exits = []
    unknown_exits = []
    for exit in used_graph_vertex['exits']:
        if used_graph_vertex['exits'][exit] == "?":
            unknown_exits.append(exit)
        elif used_graph_vertex['exits'][exit] != None:
            known_exits.append(exit)
    
    # Select array
    if len(unknown_exits) == 0:
        return False
    elif len(unknown_exits) > 0:
        used_array = unknown_exits 
    else: 
        used_array = known_exits
    # - - - - 

    # Pick random direction
    selected_direction = used_array[random.randint(0, len(used_array) -1 )]


    if LIVE_print:
        print(f'-  🎞  🎞  🎞  - KNOWN EXITS/\n{known_exits}')
        print(f'-  ❓  ❓  ❓  - UNKNOWN EXITS/\n{unknown_exits}')

    # return
    return selected_direction
