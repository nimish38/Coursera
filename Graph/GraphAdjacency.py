class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        if v in self.graph.keys():
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) or (u in self.graph[v])
        return False
