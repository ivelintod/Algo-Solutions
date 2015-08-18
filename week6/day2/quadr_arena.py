class Quadruplets:

    def __init__(self, num, vectors):
        self.num = num
        self.vectors = vectors
        self.size = len(self.vectors[0]) ** 2
        self.index = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, index, data):
        ind = self.hashfunction(key, self.size)

        if index[ind] == None:
            index[ind] = key
            data[ind] = 1
        else:
            if index[ind] == key:
                data[ind] += 1
            else:
                new_ind = self.rehash(ind, self.size)
                while index[new_ind] != None and index[new_ind] != key:
                    new_ind = self.rehash(new_ind, self.size)
                if index[new_ind] == None:
                    index[new_ind] = key
                    data[new_ind] = 1
                else:
                    data[new_ind] += 1

    def check_key_presence(self, key, index, data):
        ind = self.hashfunction(key, self.size)

        if index[ind] == key:
            return data[ind]

        elif index[ind] == None:
            return False

        else:
            new_ind = self.rehash(ind, self.size)
            while index[new_ind] != None and index[new_ind] != key and new_ind != ind:
                new_ind = self.rehash(new_ind, self.size)

            if index[new_ind] == None:
                return False
            elif index[new_ind] == key:
                return data[new_ind]
            else:
                return False

    def count_zeros(self):

        for i in self.vectors[2]:
            for j in self.vectors[3]:
                self.put(i + j, self.index, self.data)

        count_z = 0

        for i in self.vectors[0]:
            for j in self.vectors[1]:
                if self.check_key_presence(-(i + j), self.index, self.data):
                    count_z += self.check_key_presence(-(i + j), self.index, self.data)

        return count_z


def main():

    num = int(input())
    temp = []
    for i in range(4):
        j = input()
        temp.append([int(x) for x in j.split()])

    q = Quadruplets(num, temp)
    print(q.count_zeros())

if __name__ == '__main__':
    main()
