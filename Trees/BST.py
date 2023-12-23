class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

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



