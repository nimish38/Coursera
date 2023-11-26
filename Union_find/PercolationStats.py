from Union_find import Percolates
import random
import numpy as np

class PercolationStats:

    def __init__(self, n, t):
        self.size = n
        self.trials = t
        self.results = []
        self.opened

        for experiment in range(self.trials):
            Percolation = Percolates(self.size)
            while not Percolation.percolates():
                row = random.randrange(1, n)
                col = random.randrange(1, n)
                if not Percolation.isOpen(row, col):
                    Percolation.open(row, col)
            self.results.append(Percolation.numberOfOpenSites() / self.size * self.size)

    def mean(self):
        return np.mean(np.array(self.results))

    def stddev(self):
        return np.std(np.array(self.results))

    def confidenceLo(self):
        return self.mean() - (1.96 * self.stddev() / self.trials**0.5)

    def confidenceLo(self):
        return self.mean() + (1.96 * self.stddev() / self.trials**0.5)
