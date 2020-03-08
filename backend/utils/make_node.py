# IMPORTS
import json
import pdb

def make_node(room_id, graph, FILENAME):
    '''
        generic node maker for graph -- aka INSTANCE_graph or GOD_graph

    '''
    # if not graph:
    #     return 'ERROR'
    # print('in make node')
    # - - - - 

    # Case: None
    if graph == None:
        # Make data
        node_data = {
            'room_id': -1,
            "n" : 'TEST',
            "s" : 'TEST',
            "e" : 'TEST',
            "w" : 'TEST',
        }

        # OPEN and write
        print(FILENAME)
        with open(FILENAME, 'w+') as file: 
            json.dump(node_data, file)
    else:
        # Read Node
        
        print(f'NEED UPDATE NODE')
        
        pdb.set_trace()
        
        

    

    