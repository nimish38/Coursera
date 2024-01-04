class Trie:
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current.keys():
                return False
            current = current[char]
        if self.end_symbol in current.keys() and current[self.end_symbol]:
            return True
        return False

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
