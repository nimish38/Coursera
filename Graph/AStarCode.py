import random


def heuristic(next, dest):
    return abs(next.x - dest.x) + abs(next.y - dest.y)


def a_star_search(traffic_grid, src, dest):
    pq = PriorityQueue()
    pq.push(0, src)
    pred = dict()
    pred[src] = None
    cost = dict()
    cost[src] = 0
    visited = set()

    while not pq.empty():
        lowest = pq.pop()
        if lowest == dest:
            break
        if lowest in visited:
            continue
        visited.add(lowest)
        for neighbor in traffic_grid.neighbors(lowest):
            tot_cost = cost[lowest] + neighbor.cost()
            if neighbor not in cost or tot_cost < cost[neighbor]:
                cost[neighbor] = tot_cost
                prio = tot_cost + heuristic(lowest, neighbor)
                pq.push(prio, neighbor)
                pred[neighbor] = lowest

    path = []
    final = dest
    while final:
        path.append(final)
        final = pred[final]
    return path[::-1]

    # don't touch below this line


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        bucket = random.randint(1, 2)
        cost = random.randint(1, 5)
        if bucket == 2:
            cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results


def main():
    print_search(4, 4, Tile(0, 0), Tile(3, 3))
    print_search(8, 8, Tile(0, 4), Tile(7, 4))


def print_search(w, h, src, dest):
    print(f"creating grid with width {w} and height {h}")
    g = TrafficGrid(w, h)
    print(g)
    path = a_star_search(g, src, dest)
    print(f"shortest path from {src} to {dest}: {path}")
    print("----")


main()
