class Trie:
    def words_with_prefix(self, prefix):
        curr = self.root
        words = list()
        for char in prefix:
            if char not in curr.keys():
                return words
            curr = curr[char]
        return list(set(self.search_level(curr, prefix, words)))

    def search_level(self, cur, cur_prefix, words):
        for element in cur.keys():
            if element == self.end_symbol:
                words.append(cur_prefix)
            else:
                words.extend(self.search_level(cur[element], cur_prefix + element, words))
        return words


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
