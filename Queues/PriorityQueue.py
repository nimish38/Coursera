class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return True if len(self.elements) == 0 else False

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min_index_so_far = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min_index_so_far][0]:
                min_index_so_far = i

        return self.elements.pop(min_index_so_far)[1]

        # don't touch below this line


def main():
    pq = PriorityQueue()
    pq.push(10, {"name": "A street", "priority": 10})
    pq.push(1, {"name": "B street", "priority": 1})
    pq.push(3, {"name": "C street", "priority": 3})
    pq.push(2, {"name": "D street", "priority": 2})
    pq.push(8, {"name": "E street", "priority": 8})
    pq.push(7, {"name": "F street", "priority": 7})
    pq.push(6, {"name": "G street", "priority": 6})
    pq.push(7, {"name": "H street", "priority": 7})
    pq.push(7, {"name": "I street", "priority": 7})
    pq.push(5, {"name": "J street", "priority": 5})

    while not pq.empty():
        rt = pq.pop()
        print(f"Popping route {rt['name']}. Traffic delay: {rt['priority']} minutes")


main()
