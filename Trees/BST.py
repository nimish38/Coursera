class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def get_min(self):
        currNode = self
        while currNode.left:
            currNode = currNode.left
        return currNode.val

    def get_max(self):
        currNode = self
        while currNode.right:
            currNode = currNode.right
        return currNode.val

    def insert(self, val):
        if not self.val:
            self.val = val
        else:
            if self.val > val:
                if not self.left:
                    self.left = BSTNode(val)
                else:
                    self.left.insert(val)

            if self.val < val:
                if not self.right:
                    self.right = BSTNode(val)
                else:
                    self.right.insert(val)



