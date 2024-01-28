def get_path(dest, predecessors):
    path = [dest]
    while dest in predecessors.keys():
        path.append(predecessors[dest])
        dest = predecessors[dest]
    path.reverse()
    return path


def test(dest, predecessors):
    print(f"using dest: {dest}")
    print(f"using predecessors: {predecessors}")
    path = get_path(dest, predecessors)
    print(f"path: {path}")
    print("----")


def main():
    dest = "a"
    predecessors = {"a": "b", "b": "c", "c": "d"}
    test(dest, predecessors)

    dest = "a"
    predecessors = {"a": "d", "b": "c", "d": "b"}
    test(dest, predecessors)

    dest = "d"
    predecessors = {
        "a": "d",
    }
    test(dest, predecessors)

    dest = "a"
    predecessors = {
        "a": "d",
    }
    test(dest, predecessors)


main()
