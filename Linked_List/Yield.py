class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self, node):
        if self.head:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = node
        else:
            self.head = node

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
