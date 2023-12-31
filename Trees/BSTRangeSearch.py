class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        gamer_tags = []
        stack = list()

        stack.append(self)
        while len(stack) > 0:
            top = stack.pop()
            if lower_bound <= top.val.gamertag <= upper_bound:
                gamer_tags.append(top.val)

            if top.right and top.val.gamertag < upper_bound:
                stack.append(top.right)

            if top.left and top.val.gamertag > lower_bound:
                stack.append(top.left)


        return gamer_tags


    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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
