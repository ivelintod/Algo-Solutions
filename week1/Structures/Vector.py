class Vector:

    def __init__(self):
        self.vector = [None]
        self.available = self.vector[:len(self.vector) // 2]
        self.reserved = self.vector[len(self.vector) // 2:]

    def __str__(self):
        return str(self.availability())

    def availability(self):
        available = []
        for i in self.vector:
            if i != None:
                available.append(i)
            else:
                break
        return availableO


    def update_available_reserved(self):
        self.available = self.vector[:len(self.vector) // 2]
        self.reserved = self.vector[len(self.vector) // 2:]

    def insert(self, index, value):
        if index > len(self.availability()) - 1 or index < 0:
            return False
        if None in self.vector:
            j = len(self.availability()) - 1
            for i in range(len(self.availability()) - index):
                self.vector[j + 1] = self.vector[j]
                j -= 1
            self.vector[index] = value
        else:
            self.vector += len(self.vector) * [None]
            self.update_available_reserved()
            self.insert(index, value)

    def add(self, value):
        if None in self.available:
            add_spot = self.available.index(None)
            self.available[add_spot] = value
        elif None in self.reserved:
            add_spot = self.reserved.index(None)
            self.reserved[add_spot] = value
        else:
            self.vector += len(self.vector) * [None]
            self.update_available_reserved()
            self.add(value)
        self.vector = self.available + self.reserved

    def remove(self, index):
        if index > len(self.availability()) or index < 0:
            return False
        else:
            j = index
            for i in range(len(self.available) + 1 - (index)):
                self.vector[j] = self.vector[j + 1]
                j += 1
            self.vector[len(self.availability()) - 1] = None

    def pop(self):
        index = len(self.availability()) - 1
        self.vector[index] = None

    def size(self):
        return len(self.availability())

    def capacity(self):
        return len(self.vector)

    def get(self, index):
        return self.vector[index]





def main():
    v = Vector()
    v.add('h')
    v.add('z')
    v.add('p')
    v.add('m')
    v.add('o')
    v.add('k')
    v.add('i')
    v.add('t')
    v.add('q')
    v.add('c')
    #v.remove(4)
    print(v)
    print(str(v.vector))
    print(v.size())
    print(v.capacity())

if __name__ == '__main__':
    main()
