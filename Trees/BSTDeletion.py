class BSTNode:
    def get_min_larger_node(self):
        currNode = self
        while currNode.left:
            currNode = currNode.left
        return currNode

    def delete(self, val):
        if not self.val:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if val == self.val:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            else:
                replaced_self = self.right.get_min_larger_node()
                self.val = replaced_self.val
                self.right = self.right.delete(replaced_self.val)
        return self

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
