# refer https://www.youtube.com/watch?v=gaBWn0gGM4Q&ab_channel=SayanMondal

class Percolation:
    def __init__(self, n):
        self.openSites = []
        self.size = n
        self.cntOpenedSites = 0
        self.TOP = 0
        self.BOTTOM = n + 1
        self.princetonAPIQf = [self.TOP, self.OpenSites, self.BOTTOM]
        for i in range(n):
            row = [False]*n
            self.grid.append(row)

    def isOpen(self, row, col):
        return self.openSites[row - 1][col - 1]

    def getGridIndex(self, row, col):
        # return site number as per problem naming convention ie (2,3) corresponds to site 6
        return self.size*(row - 1) + col

    def performUnion(self, site1, site2):
        # Princeton API which does union of two sites
        return

    def isConnected(self, site1, site2):
        # Princeton API which tells if 2 sites are connected are not
        return site1 and site2

    def checkBounds(self, row, col):
        if row < 0 or row > self.size or col < 0 or col > self.size:
            raise IndexError
        return True

    def open(self, row, col):
        # check for exceptions
        self.checkBounds(row, col)
        if not self.isOpen(row, col):
            # if the site is closed, open the site and increment opened sites count
            self.OpenSites[row - 1][col - 1] = True
            self.cntOpenedSites += 1

        # if it is top row of sites, perform its Union with virtual Top element
        if row == 1:
            self.performUnion(self.getGridIndex(row, col), self.TOP)

        # if it is bottom row of sites, perform its Union with virtual Bottom element
        if row == self.size:
            self.performUnion(self.BOTTOM, self.getGridIndex(row, col))

        # Now check all neighboring sites and if open perform union of sites
        # left neighbor
        if row > 1 and self.isOpen(row - 1, col):
            self.performUnion(self.getGridIndex(row - 1, col), self.getGridIndex(row, col))
        # right neighbor
        if row < self.size and self.isOpen(row + 1, col):
            self.performUnion(self.getGridIndex(row +1, col), self.getGridIndex(row, col))
        # top neighbor
        if col > 1 and self.isOpen(row, col - 1):
            self.performUnion(self.getGridIndex(row, col - 1), self.getGridIndex(row, col))
        # bottom neighbor
        if col < self.size and self.isOpen(row, col + 1):
            self.performUnion(self.getGridIndex(row, col + 1), self.getGridIndex(row, col))

    def isFull(self, row, col):
        return self.isConnected(self.getGridIndex(row, col), self.TOP)

    def numberOfOpenSites(self):
        return self.cntOpenedSites

    def percolates(self):
        # System percolates when virtual top and bottom elements are connected
        return self.isConnected(self.TOP, self.BOTTOM)


    def printGrid(self):
        for i in range(self.size):
            print(self.grid[i])


MySite = Percolation(3)
MySite.printGrid()
