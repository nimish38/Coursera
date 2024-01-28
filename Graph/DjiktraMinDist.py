def get_min_dist_node(distances, unvisited):
    shortest = float("inf")
    shortest_node = ''
    for node in unvisited:
        if distances[node] < shortest:
            shortest = distances[node]
            shortest_node = node
    return shortest_node

    # don't touch below this line

def test(distances, unvisited):
    print("using distances:")
    for k in sorted(distances):
        print(f" - {k}: {distances[k]}")
    print("using unvisited:")
    for k in sorted(unvisited):
        print(f" - {k}")
    min_dist_node = get_min_dist_node(distances, unvisited)
    print(f"min_dist_node: {min_dist_node}")
    print("----")


def main():
    distances = {"a": 4, "b": 2, "c": 3, "d": 1}
    unvisited = {"a", "c"}
    test(distances, unvisited)

    distances = {"a": 1, "b": 2, "c": 2, "d": 1}
    unvisited = {"a", "c"}
    test(distances, unvisited)

    distances = {"a": 1, "b": 2, "c": 2, "d": 1}
    unvisited = {"b", "d"}
    test(distances, unvisited)


main()
