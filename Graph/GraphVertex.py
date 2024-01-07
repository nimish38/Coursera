class Graph:
    def __init__(self, num_vertices):
        self.graph = list()
        for i in range(num_vertices):
            self.graph.append([False] * num_vertices)
        #print(num_vertices, self.graph)

    def add_edge(self, u, v):
        self.graph[u][v] = self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
