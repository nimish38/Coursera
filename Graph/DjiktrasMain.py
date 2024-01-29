def dijkstra(graph, src, dest):
    unvisited = set()
    predecessor = {}
    distances = {}

    for node in graph.keys():
        if node == src:
            distances[node] = 0
        else:
            unvisited.add(node)
            distances[node] = float("INF")

    while len(unvisited) > 0:
        closest_node = get_min_dist_node(graph[src], unvisited)
        unvisited.remove(closest_node)
        predecessor[closest_node] = src
        distances[closest_node] = graph[src][closest_node]
        if closest_node == dest:
            return get_path(dest, predecessor)
        else:
            for neighbor in graph[closest_node].keys():
                if neighbor in unvisited:
                    first_distance = distances[closest_node]
                    second_distance = graph[closest_node][neighbor]
                    combined_dist = first_distance + second_distance
                    if combined_dist < distances[neighbor]:
                        distances[neighbor] = combined_dist
                        predecessor[neighbor] = closest_node
        src = closest_node


def get_path(dest, predecessors):
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


def get_min_dist_node(distances, unvisited):
    min_dist = float("inf")
    min_dist_node = None
    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            min_dist_node = v
    return min_dist_node


def main():
    graph = {
        "a": {"b": 4, "c": 1},
        "b": {"a": 4, "d": 3, "e": 8},
        "c": {"a": 1, "d": 2, "f": 6},
        "d": {"c": 2, "b": 3, "e": 4},
        "e": {"d": 4, "b": 8, "g": 2},
        "f": {"c": 6, "g": 8},
        "g": {"f": 8, "e": 2},
    }
    print("using graph:")
    for v in graph:
        print(f"- vertex {v}: {graph[v]}")
    print_path(graph, "a", "g")
    print_path(graph, "b", "c")

    graph = {
        "s": {"a": 2, "b": 1},
        "a": {"s": 3, "b": 4, "c": 8},
        "b": {"s": 4, "a": 2, "d": 2},
        "c": {"a": 2, "d": 7, "t": 4},
        "d": {"b": 1, "c": 11, "t": 5},
        "t": {"c": 3, "d": 5},
    }
    print("using graph:")
    for v in graph:
        print(f"- vertex {v}: {graph[v]}")
    print_path(graph, "s", "t")
    print_path(graph, "a", "d")


def print_path(graph, src, dest):
    print(f"shortest path from {src} to {dest}: {dijkstra(graph, src, dest)}")


main()
