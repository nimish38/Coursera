class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) > 0:
            head = self.items[len(self.items) - 1]
            del self.items[len(self.items) - 1]
            return head
        return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        return None

    def size(self):
        return len(self.items)
