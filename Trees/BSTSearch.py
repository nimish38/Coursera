class BSTNode:
    def exists(self, val):
        if self.val:
            if self.val == val:
                return True
            if self.val < val:
                if self.right:
                    return self.right.exists(val)
                return False
            if self.val > val:
                if self.left:
                    return self.left.exists(val)
                return False
        return False


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
