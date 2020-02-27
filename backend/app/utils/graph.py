class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, title, description, coordinates, elevation, terrain, items, exits, messages):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = {}
        self.vertices[vertex]["room_id"] = vertex
        self.vertices[vertex]["title"] = title
        self.vertices[vertex]["description"] = description
        self.vertices[vertex]["coordinates"] = coordinates
        self.vertices[vertex]["elevation"] = elevation
        self.vertices[vertex]["terrain"] = terrain
        self.vertices[vertex]["items"] = items
        self.vertices[vertex]["exits"] = exits
        self.vertices[vertex]["messages"] = messages

    def add_edge(self, v1, direction, v2):
        """
        Add a directed edge to the graph.
        """
        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1]["exits"][direction] = v2
        else:
            raise IndexError("That vertex does not exist")