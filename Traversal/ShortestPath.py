class Graph:
    def bfs_path(self, start, end):
        routes = [([start], 0)]
        while len(routes) > 0:
            last = routes.pop()
            current, level = last[0], last[1]
            for neighbor in self.graph[current[-1]]:
                new_route = current + [neighbor]
                if neighbor == end:
                    return new_route
                routes.append((new_route, level + 1))
        return None


    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
