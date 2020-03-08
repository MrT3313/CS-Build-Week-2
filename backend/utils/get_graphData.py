# IMPORTS
import pdb

# PRINT 
LIVE_print = True
DEBUG_print = True

def get_graphData(current_room, FILENAME__INSTANCE_graph):
    # GOD
    with open('GOD_graph.json', 'r') as GOD_file: 
        try: 
            data = json.load(GOD_file)
            
            GOD_graph = data
        except:
            if DEBUG_print:
                print(f'---DEBUG--- NO GOD_graph DATA')
            GOD_graph = None
        finally:
            GOD_file.close()
        if DEBUG_print:
            print(f'---DEBUG--- DATA: GOD_graph/\n{GOD_graph}')
    # - - - - 

    # INSTANCE
    with open(FILENAME__INSTANCE_graph, 'r') as INSTANCE_file: 
        try: 
            data = json.load(INSTANCE_file)
            
            INSTANCE_graph = data
        except:
            if DEBUG_print:
                print(f'---DEBUG--- NO GOD_graph DATA')
            INSTANCE_graph = None
        finally:
            INSTANCE_file.close()
        if DEBUG_print:
            print(f'---DEBUG--- DATA: INSTANCE_graph/\n{INSTANCE_graph}')
    # - - - - 

    # Debug
    if DEBUG_print:
        print(f'---DEBUG--- RESULT: GOD_graph/\n{GOD_graph}')
        if GOD_graph is not None:
            for item in GOD_graph:
                print('GOD item',item)
        print(f'---DEBUG--- RESULT: INSTANCE_graph/\n{INSTANCE_graph}')
    # - - - - 

    # Return
    return GOD_graph, INSTANCE_graph
