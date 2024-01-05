class Trie:
    def find_matches(self, document):
        matches = list()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                if document[j] not in level.keys():
                    break
                else:
                    level = level[document[j]]
                if self.end_symbol in level.keys():
                    matches.append(document[i:j+1])
        return set(matches)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
