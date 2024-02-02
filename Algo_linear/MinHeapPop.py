class MinHeap:
    def pop(self):
        if len(self.elements) == 0:
            return None
        if len(self.elements) == 1:
            return self.elements.pop()
        else:
            top = self.elements[0]
            self.elements[0] = self.elements[len(self.elements) - 1]
            del self.elements[len(self.elements) - 1]
            self.bubble_down(0)
            return top

    def bubble_down(self, index):
        length = len(self.elements)
        leftIndex, rightIndex = (2 * index) + 1, (2 * index) + 2
        parent = self.elements[index][0]
        smallerIndex = -1
        smallerValue = float("inf")
        if leftIndex < length:
            leftKid = self.elements[leftIndex][0]
            if leftKid < parent:
                smallerIndex = leftIndex
                smallerValue = leftKid

        if rightIndex < length:
            rightKid = self.elements[rightIndex][0]
            if rightKid < smallerValue:
                smallerIndex = rightIndex

        if smallerIndex != -1:
            self.elements[index], self.elements[smallerIndex] = self.elements[smallerIndex], self.elements[index]
            self.bubble_down(smallerIndex)


    # don't touch below this line

    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        parent_priority = self.elements[parent_index][0]
        index_priority = self.elements[index][0]
        if parent_priority > index_priority:
            self.elements[parent_index], self.elements[index] = (
                self.elements[index],
                self.elements[parent_index],
            )
            self.bubble_up(parent_index)

    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0][1]


def test_push(min_heap, priority, value):
    print(f"Pushing {value} with priority {priority}")
    min_heap.push(priority, value)
    print(f"{min_heap.peek()} is at the top of the heap")


def test_pop(min_heap):
    tup = min_heap.pop()
    if tup is None:
        return False
    print(f"Popped {tup[1]} with priority {tup[0]}")
    return True


def main():
    min_heap = MinHeap()
    test_push(min_heap, 10, "A street")
    test_push(min_heap, 3, "C street")
    test_push(min_heap, 8, "E street")
    test_push(min_heap, 6, "G street")
    test_push(min_heap, 7, "H street")
    test_push(min_heap, 2, "D street")
    print("========")

    while test_pop(min_heap):
        pass
    print("Done popping")


main()
