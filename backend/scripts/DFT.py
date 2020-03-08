# IMPORTS
import pdb 
import json

# SCRIPTS
from utils.make_node import make_node
# from ..utils.make_node import make_node
# from ..utils.make_node import make_node

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
        print(f'---DEBUG--- current_room/\n{current_room}')

    room_id = current_room['room_id']
    
    # What do our graphs have??
    # Open GOD_graph
    with open(FILENAME__GOD_graph, 'w+') as GOD_file: 
        try: 
            data = json.load(GOD_file)
            if DEBUG_print:
                print(f'---DEBUG--- GOD_Graph HAS data')
                ## ⏫ we know it already exists so its not going to 
                ## make a second ont but insteas just open the one 
                ## we have in 'read / write'

            # Set appropriate data
            GOD_graph = data
            INSTANCE_graph = None
            # - - - - 
        except:
            # Set appropriate data
            GOD_graph = None
            FILENAME__GOD_graph = None
            # - - - -
            if DEBUG_print:
                print(f'---DEBUG--- GOD_graph does NOT contain this point')
            # Try instance graph => technically it should never be in the 
            # instance graph and not the god graph
        
            # Open INSTANCE__graph
            with open(FILENAME__INSTANCE_graph, 'w+') as INSTANCE_file: 
                try: 
                    data = json.load(INSTANCE_file)
                    if DEBUG_print:
                        print(f'---DEBUG--- INSTANCE__graph HAS data')
                        ## ⏫ we know it already exists so its not going to 
                        ## make a second ont but insteas just open the one 
                        ## we have in 'read / write'

                        # Set appropriate data => aka dont reset GOD_graph here ....
                        INSTANCE__graph = data
                except:
                    # Set appropriate data
                    INSTANCE__graph = None
                    FILENAME__GOD_graph = 'GOD_graph.txt'
                    # - - - - 

                    if DEBUG_print:
                        print(f'---DEBUG--- INSTANCE__graph does NOT contain this point')
                    if LIVE_print:
                        print(f'-  👷🏼‍♂️  👷🏼‍♂️  👷🏼‍♂️  - We need to make a node for GOD_graph & INSTNCE_graph')

                    # Make GOD node
                    GOD_RESULT_make_node = make_node(room_id, GOD_graph, FILENAME__GOD_graph)
                    pdb.set_trace()
                    INSTANCE_RESULT_make_node = make_node(room_id, INSTANCE__graph, FILENAME__INSTANCE_graph)
                    


                    print(f'-- END -- ')
                    pdb.set_trace()






        