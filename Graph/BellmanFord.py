def bellman_ford(graph, src, dest):
    distances = {}

    for node in graph.keys():
        if node == src:
            distances[node] = 0
        else:
            distances[node] = float("inf")

    for i in range(len(graph)):
        for u in graph.keys():
            for v in graph[u]:
                first_dist = distances[u]
                second_dist = graph[u][v]
                combined_dist = first_dist + second_dist
                if combined_dist < distances[v]:
                    distances[v] = combined_dist
    for u in graph.keys():
        for v in graph[u]:
            first_dist = distances[u]
            second_dist = graph[u][v]
            combined_dist = first_dist + second_dist
            if combined_dist < distances[v]:
                raise Exception('Negative cycle detected!')

    return distances[dest]

def main():
    graph = {
        "s": {"a": 5, "c": -2},
        "a": {"b": 1},
        "b": {"d": -1, "t": 3},
        "c": {"a": 2, "b": 4, "d": 3},
        "d": {"t": 1},
        "t": {},
    }
    print("using graph:")
    for v in graph:
        print(f"- vertex {v}: {graph[v]}")
    print_path(graph, "s", "t")
    print_path(graph, "a", "t")
    print_path(graph, "b", "t")
    print_path(graph, "t", "t")

    print("-----")

    graph = {"a": {"b": -1}, "b": {"c": -2}, "c": {"a": -1, "d": 3}, "d": {}}
    for v in graph:
        print(f"- vertex {v}: {graph[v]}")
    print_path(graph, "a", "d")


def print_path(graph, src, dest):
    try:
        print(f"shortest path from {src} to {dest}: {bellman_ford(graph, src, dest)}")
    except Exception as e:
        print(e)


main()
