class BST:

    def __init__(self, length, seq):
        self.length = length
        self.seq = seq
        self.seq.insert(0, None)
        self.visited_roots = list()

    def check_BST(self, ind):
        if self.seq[ind] != 0:
            self.visited_roots.append(self.seq[ind])
            if ind * 2 < self.length + 1 and self.seq[ind * 2] < self.seq[ind]:
                print ind
                self.check_BST(ind * 2)
            elif ind * 2 < self.length + 1 and self.seq[ind * 2] > self.seq[ind]:
                return 'NO'

            if ind * 2 + 1 < self.length + 1:
                if self.seq[ind * 2 + 1] == 0:
                    pass
                else:
                    if self.seq[ind * 2 + 1] < self.seq[ind]:
                        return 'NO'
                    print self.visited_roots
                    for el in self.visited_roots[:len(self.visited_roots) - 1]:
                        if self.seq[ind * 2 + 1] > el:
                            print 'ok'
                            return 'NO'
                    self.visited_roots = self.visited_roots[:len(self.visited_roots) - 1]

            self.visited_roots = self.visited_roots[:len(self.visited_roots) - 1]

    def BST(self, ind):
        valid = 'YES'
        self.visited_roots.append(self.seq[ind])
        current = self.seq[ind]
        if ind * 2 < self.length + 1:
            if self.seq[ind * 2] > self.seq[ind]:
                valid = 'NO'
            else:
                valid = self.BST(ind * 2)

        if ind * 2 + 1 < self.length + 1:




        return valid


def main():
    b = BST(15, [8, 5, 15, 1, 0, 10, 18, 0, 2, 0, 0, 0, 12, 16, 20])
    print(b.check_BST(1))

if __name__ == '__main__':
    main()
