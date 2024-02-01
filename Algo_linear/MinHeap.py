class MinHeap:
    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return
        if index % 2:
            parent = index // 2
        else:
            parent = (index // 2) - 1
        if self.elements[parent][0] > self.elements[index][0]:
            self.elements[parent], self.elements[index] = self.elements[index], self.elements[parent]
            self.bubble_up(parent)

        # don't touch below this line

    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0][1]


def test(min_heap, priority, value):
    print(f"Pushing {value} with priority {priority}")
    min_heap.push(priority, value)
    print(f"{min_heap.peek()} is at the top of the heap")


def main():
    min_heap = MinHeap()
    test(min_heap, 10, "A street")
    test(min_heap, 3, "C street")
    test(min_heap, 8, "E street")
    test(min_heap, 6, "G street")
    test(min_heap, 7, "H street")
    test(min_heap, 2, "D street")
    test(min_heap, 1, "B street")
    test(min_heap, 7, "I street")
    test(min_heap, 5, "J street")


main()
