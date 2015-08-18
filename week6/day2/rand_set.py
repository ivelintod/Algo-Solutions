import random

class RS:

    def __init__(self):
        self.size = 11
        self.index = [None] * self.size
        self.count_el = 0

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 3) % size

    def expansion_check(self):
        if self.count_el == self.size:
            self.size *= 2
            temp = self.index
            self.index = [None] * self.size
            self.count_el = 0
            for i in temp:
                if i != None and i != 'DELETED':
                    self.insert(i)

    def reduction_check(self):
        if self.count_el == self.size/4:
            self.size /= 2
            temp = self.index
            self.index = [None] * self.size
            self.count_el = 0
            for i in temp:
                if i != None and i != 'DELETED':
                    self.insert(i)

    def insert(self, key):
        ind = self.hashfunction(key, self.size)

        if self.index[ind] == None or self.index[ind] == 'DELETED':
            self.index[ind] = key
            self.count_el += 1

        else:
            if self.index[ind] == key:
                pass

            else:
                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != 'DELETED' and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind, self.size)

                if self.index[new_ind] == None or self.index[new_ind] == 'DELETED':
                    self.index[new_ind] = key
                    self.count_el += 1
                elif self.index[new_ind] == key:
                    pass
                else:
                    #if self.count_el == self.size:
                    self.expansion_check()
                    self.insert(key)

    def remove(self, key):
        ind = self.hashfunction(key, self.size)

        if self.index[ind] == None or self.index[ind] == 'DELETED':
            print('Keyerror: {}'.format(key))

        else:
            if self.index[ind] == key:
                self.index[ind] = 'DELETED'
                self.count_el -= 1
                self.reduction_check()

            else:
                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind, self.size)

                if self.index[new_ind] == None:
                    print('Keyerror: {}'.format(key))

                elif self.index[new_ind] == key:
                    self.index[new_ind] = 'DELETED'
                    self.count_el -= 1
                    self.reduction_check()

                else:
                    print('Keyerror: {}'.format(key))

    def contains(self, key):
        ind = self.hashfunction(key, self.size)

        if self.index[ind] == None:
            return 'false'

        else:
            if self.index[ind] == key:
                return 'true'

            else:
                new_ind = self.rehash(ind, self.size)
                while self.index[new_ind] != None and self.index[new_ind] != key and new_ind != ind:
                    new_ind = self.rehash(new_ind, self.size)

                if self.index[new_ind] == None:
                    return 'false'

                elif self.index[new_ind] == key:
                    return 'true'

                else:
                    return 'false'

    def random(self):
        i = random.randint(1, 1000)
        ind = self.hashfunction(i, self.size)
        while self.index[ind] == None or self.index[ind] == 'DELETED':
            i = random.randint(1, 1000)
            ind = self.hashfunction(i, self.size)
        return self.index[ind]




def main():
    h = RS()
    for i in range(10):
        h.insert(i)
    h.insert(30)
    h.remove(87)
    h.remove(87)
    h.remove(1)
    h.remove(2)
    h.remove(3)
    h.remove(0)
    h.remove(4)
    h.remove(30)
    h.remove(5)
    h.remove(6)
    h.remove(7)
    h.insert(3)
    h.insert(50)
    h.insert(39)
    h.insert(39)
    h.insert(41)
    print(h.index)
    print(h.contains(15))
    print(h.random())

if __name__ == '__main__':
    main()
