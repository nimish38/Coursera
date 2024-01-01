class BSTNode:
    def height(self):
        if not self:
            return 0
        leftHeight, rightHeight = 0, 0
        if self.left:
            leftHeight = self.left.height()
        if self.right:
            rightHeight = self.right.height()
        return 1 + max(leftHeight, rightHeight)



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
