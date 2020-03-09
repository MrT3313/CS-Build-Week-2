# IMPORTS
import pdb
import json

# PRINT 
LIVE_print = True
DEBUG_print = True

def get_graphData(current_room, FILENAME__INSTANCE_graph):
    # GOD
    print('start getting GOD data')
    print('GOD_graph.json')

    with open('GOD_graph.json', 'r+') as GOD_file: 
    # with open('GOD_graph.json', 'r+') as GOD_file: 
        try: 
            data = json.load(GOD_file)
            GOD_graph_data = data
        except:
            if DEBUG_print:
                print(f'---DEBUG--- NO GOD_graph DATA')
            GOD_graph_data = None
        # Debug
        if DEBUG_print:
            print(f'---DEBUG--- DATA: GOD_graph/\n{GOD_graph_data}')
    # - - - - 
    
    # INSTANCE
    print('Start getting json data')
    print(FILENAME__INSTANCE_graph)
    with open(FILENAME__INSTANCE_graph, 'r+') as INSTANCE_file: 
        try: 
            data = json.load(INSTANCE_file)
            
            INSTANCE_graph_data = data
        except:
            if DEBUG_print:
                print(f'---DEBUG--- NO INSTANCE_graph DATA')
            INSTANCE_graph_data = None
        finally:
            INSTANCE_file.close()
        if DEBUG_print:
            print(f'---DEBUG--- DATA: INSTANCE_graph/\n{INSTANCE_graph_data}')
    # - - - - 

    # Debug
    if DEBUG_print:
        print(f'---DEBUG--- RESULT: GOD_graph/\n{GOD_graph_data}')
        if GOD_graph_data is not None:
            for item in GOD_graph_data:
                print('GOD item',item)
        print(f'---DEBUG--- RESULT: INSTANCE_graph/\n{INSTANCE_graph_data}')
    # - - - - 
    # pdb.set_trace()
    # Return
    return GOD_graph_data, INSTANCE_graph_data
