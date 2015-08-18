class KI:

    def __init__(self):
        self.index = [None] * 11
        self.size = 11
        self.count = 0

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def expansion(self):
        if self.size == self.count:
            self.size *= 2
            temp = self.index
            self.index = [None] * self.size
            self.count = 0
            for el in temp:
                if el != None and el != 'DELETED':
                    self.insert(el)
            del temp

    def reduction(self):
        if self.count == self.size / 3:
            self.size /= 2
            temp = self.index
            self.index = [None] * self.size
            self.count = 0
            for el in temp:
                if el != None and el != 'DELETED':
                    self.insert(el)
            del temp

    def insert(self, key):
        ind = self.hashfunction(key)

        if self.index[ind] == None or self.index[ind] == 'DELETED':
            self.index[ind] = key
            self.count += 1

        else:
            if self.index[ind] == key:
                pass

            else:
                new_ind = self.rehash(ind)
                while self.index[new_ind] != None and self.index[new_ind] != 'DELETED' and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind)

                if self.index[new_ind] == None or self.index[new_ind] == 'DELETED':
                    self.index[new_ind] = key
                    self.count += 1

                elif self.index[new_ind] == key:
                    pass

                else:
                    self.expansion()
                    self.insert(key)
                    #self.count += 1

    def remove(self, key):
        ind = self.hashfunction(key)

        if self.index[ind] == None or self.index[ind] == 'DELETED':
            return False

        else:
            if self.index[ind] == key:
                self.index[ind] = 'DELETED'
                self.count -= 1
                self.reduction()

            else:
                new_ind = self.rehash(ind)
                while self.index[new_ind] != None and self.index[new_ind] != 'DELETED' and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind)

                if self.index[new_ind] == None or self.index[new_ind] == 'DELETED':
                    return False

                elif self.index[new_ind] == key:
                    self.index[new_ind] = 'DELETED'
                    self.count -= 1
                    self.reduction()
                else:
                    return False

    def contains(self, key):
        ind = self.hashfunction(key)

        if self.index[ind] == None or self.index[ind] == 'DELETED':
            return False

        else:
            if self.index[ind] == key:
                return True

            else:
                new_ind = self.rehash(ind)
                while self.index[new_ind] != None and self.index[new_ind] != 'DELETED' and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind)

                if self.index[new_ind] == None or self.index[new_ind] == 'DELETED':
                    return False

                elif self.index[new_ind] == key:
                    return True

                else:
                    return False

def K_inter(num, lists):
    original = KI()
    compare = KI()
    for el in lists[0][1]:
        original.insert(el)

    for i in range(1, num):
        for el in lists[i][1]:
            compare.insert(el)

        for elem in original.index:

            if elem != None and elem != 'DELETED':
                if not compare.contains(elem):
                    original.remove(elem)

        compare.count = 0
        compare.size = 11
        compare.index = [None] * compare.size

    for i in original.index:
        if i != None and i != 'DELETED':
            print(i)



def main():
    k = K_inter(3, ([5, (2, 5, 10, 3, 1)], [8, (7, 13, 3, 9, 2, 55, 47, 10)], [3, (42, 2, 3)]))




if __name__ == '__main__':
    main()
