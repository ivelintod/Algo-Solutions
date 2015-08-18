class Hashmap:

    def __init__(self):
        self.size = 11
        self.eval = 2
        self.count_space = 0
        self.index = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, value):
        ind = self.hashfunction(key, self.size)

        if self.index[ind] == key:
            self.data[ind] = value #replace
        else:

            if self.index[ind] == None:
                self.index[ind] = key
                self.data[ind] = value

            else:

                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != key:
                    new_ind = self.rehash(new_ind, self.size)
                if self.index[new_ind] == key:
                    self.data[new_ind] = value #replace
                elif self.index[new_ind] == None:
                    self.index[new_ind] = key
                    self.data[new_ind] = value

        self.count_space += 1

        if self.count_space == self.size:
            self.index += [None] * self.eval
            self.data += [None] * self.eval
            self.size += self.eval
            self.eval *= 2

    def get(self, key):
        ind = self.hashfunction(key, self.size)

        if self.index[ind] == key:
            return self.data[ind]

        elif self.index[ind] == None:
            return 'Key not found'

        else:
            new_ind = self.rehash(ind, self.size)

            while self.index[new_ind] != None and self.index[new_ind] != key and new_ind != ind:
                new_ind = self.rehash(new_ind, self.size)

            if self.index[new_ind] == None:
                return 'Key not found'
            elif self.index[new_ind] == key:
                return self.data[new_ind]
            elif new_ind == ind:
                return 'Key not found'



    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        return str([x for x in self.index if x != None])


def main():
    h = Hashmap()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    h[23] = 'kor'
    h[90] = 'dawe'
    h[33] = 'eto me'
    print(h[33])
    print h[99]
    print(h.data)
    print(h.index)


if __name__ == '__main__':
    main()
