class WD:

    def __init__(self):
        self.size = 11
        self.index = [None] * self.size
        self.data = [None] * self.size
        self.count_el = 0

    def hashfunction(self, num, size):
        return num % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def expansion(self):
        self.size *= 2
        temp = self.data
        self.index = [None] * self.size
        self.data = [None] * self.size
        self.count_el = 0
        for i in temp:
            if i != None:
                self.insert(i)
                self.count_el += 1

    def insert(self, word):
        result = ''
        for letter in word:
            result += str(ord(letter))
        result = int(result)

        ind = self.hashfunction(result, self.size)

        if self.data[ind] == None:
            self.index[ind] = result
            self.data[ind] = word
            self.count_el += 1

        else:
            if self.index[ind] == result:
                pass
            else:
                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != int(result) and new_ind != ind:
                    new_ind = self.rehash(new_ind, self.size)

                if self.index[new_ind] == None:
                    self.index[new_ind] = result
                    self.data[new_ind] = word
                    self.count_el += 1

                elif new_ind == ind:
                    self.expansion()
                    self.insert(word)

    def contains(self, word):
        result = ''
        for letter in word:
            result += str(ord(letter))
        result = int(result)

        ind = self.hashfunction(result, self.size)

        if self.index[ind] == None:
            print 'false'

        else:
            if self.index[ind] == result:
                print 'true'
            else:
                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != result and new_ind != ind:
                    new_ind = self.rehash(new_ind, self.size)

                if self.index[new_ind] == None:
                    print 'false'

                elif self.index[new_ind] == result:
                    print 'true'

                else:
                    print 'false'


def main():
    w = WD()
    w.insert('alabala')
    w.insert('asdf')
    w.contains('alabala')
    w.insert('aladin')
    w.contains('asdf')
    w.contains('aladin')
    w.insert('circle')
    w.contains('square')
    w.contains('rectangle')
    w.insert('aladin')
    print w.index
    print w.data

if __name__ == '__main__':
    main()
