class Graph:
    def unconnected_vertices(self):
        unconnected = []
        for vertex in self.graph.keys():
            if len(vertex.keys()) == 0:
                unconnected.append(vertex)
        return unconnected


    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()
