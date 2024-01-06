class Trie:
    def advanced_find_matches(self, document, variations):
        new_doc = ''
        revese_variations = {}
        for i in range(len(document)):
            if document[i] in variations.keys():
                new_val = variations[document[i]]
                new_doc += new_val
                revese_variations[new_val] = document[i]
            else:
                new_doc += document[i]
        matches = self.find_matches(new_doc)
        new_matches = set()

        for item in matches:
            x = ''
            for k in range(len(item)):
                if item[k] in revese_variations.keys():
                    x += revese_variations[item[k]]
                else:
                    x += item[k]
            new_matches.add(x)
        return  new_matches


    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    level = self.root
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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
