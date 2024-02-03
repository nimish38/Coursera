import random
class Tile:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def cost(self):
        random.seed(self.__hash__())
        return random.randint(1, 25)

        # don't touch below this line

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def main():
    t = Tile(2, 2)
    print(f"{t} - cost: {t.cost()}")

    t = Tile(5, 2)
    print(f"{t} - cost: {t.cost()}")

    t = Tile(2, 7)
    print(f"{t} - cost: {t.cost()}")

    t = Tile(8, 8)
    print(f"{t} - cost: {t.cost()}")


main()