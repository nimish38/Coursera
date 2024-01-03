class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
        current_occupancy = self.current_load()
        if current_occupancy >= 0.05:
            new_hashmap = [None for i in range(len(self.hashmap) * 10)]
            buckets = []
            for bucket in self.hashmap:
                if bucket:
                    buckets.append(bucket)
            self.hashmap = new_hashmap
            for item in buckets:
                self.insert(item[0], item[1])

    def current_load(self):
        if len(self.hashmap) > 0:
            cnt = 0
            for bucket in self.hashmap:
                if bucket:
                    cnt += 1
            return cnt / len(self.hashmap)
        return 1

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
