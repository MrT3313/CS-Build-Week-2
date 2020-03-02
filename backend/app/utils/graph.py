import pdb

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, world_graph):
        """
        Add a vertex to the graph.
        """
        # print(f'-- You are trying to add a vertex --')
        vertPrep = {
            'room_id': vertex['room_id'],
            'exits': {
                'n': "?",
                's': "?",
                'e': "?",
                'w': "?",
            },
        }

        for dir in ['n','s','e','w']:
            if dir not in vertex['exits']:
                vertPrep['exits'][dir] = None

        self.vertices[vertPrep['room_id']] = vertPrep
        # - - - - 

    def add_edge(self, v1, direction, v2):
        """
        Add a directed edge to the graph.
        """
        opposite = {"n": "s", "e": "w", "s": "n", "w": "e"}
        # print(f'PASSED V1 {v1}')
        # print(f'PASSED V2 {v2}')
        # print(f'DIRECTION {direction}')

        # print(self.vertices[v1]["exits"][direction])
        # print(self.vertices[v2]["exits"][opposite[direction]])

        self.vertices[v1]['exits'][direction] = v2
        self.vertices[v2]['exits'][opposite[direction]] = v1

        # self.print_graph()
        # pdb.set_trace()

    def print_graph(self):
        result = []
        for vert in self.vertices:
            # print(self.vertices[vert])
            result.append({vert: self.vertices[vert]})
        # print(f'-*- PRINTED GRAPH: {result}')
        return result