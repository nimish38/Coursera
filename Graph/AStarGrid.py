import random


class TrafficGrid:
    def __init__(self, width, height):
        self.height, self.width = height, width

    def in_bounds(self, tile):
        if tile.x >= 0 and self.width > tile.x and tile.y >= 0 and tile.y < self.height:
            return True
        return False

    def neighbors(self, tile):
        Tiles = [Tile(tile.x, tile.y - 1), Tile(tile.x, tile.y + 1), Tile(tile.x - 1, tile.y), Tile(tile.x + 1, tile.y)]
        adjacents = []
        for elements in Tiles:
            if self.in_bounds(elements):
                adjacents.append(elements)
        return adjacents


    # don't touch below this line

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        cost = random.randint(1, 25)
        return cost

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def main():
    print_grid(2, 2)
    print_grid(5, 5)
    print_grid(10, 10)


def print_grid(w, h):
    print(f"creating grid with width {w} and height {h}")
    print(TrafficGrid(w, h))
    print("----")


main()