class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while len(to_visit) > 0:
            node = to_visit.pop()
            visited.append(node)
            for neighbor in sorted(self.graph[node]):
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)

        return visited


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
