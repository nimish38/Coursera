class BSTNode:
    def exists(self, val):
        if self.val:
            cn = self
            while cn and cn.val != val:
                if cn.val > val:
                    cn = cn.left
                if cn.val < val:
                    cn = cn.right

            if cn and cn.val == val:
                return True
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
