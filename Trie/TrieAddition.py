class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current.keys():
                current[char] = {}
                current = current[char]
            else:
                current = current[char]
        current['*'] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
