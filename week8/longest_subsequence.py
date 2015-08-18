class LS:

    def __init__(self, length, seq):
        self.length = length
        self.seq = seq
        self.count = [1] * self.length
        #self.index = [[] for i in range(self.length)]

    def ls(self):

        ind = 1

        while ind < self.length:

            max_el = None

            for i in range(0, ind):
                if self.seq[i] < self.seq[ind]:
                    max_el = self.count[i]
                    break

            for i in range(0, ind):
                if self.seq[i] < self.seq[ind] and self.count[i] > max_el:
                    max_el = self.count[i]

            if max_el is not None:
                self.count[ind] = max_el + 1
            else:
                self.count[ind] = 1

            ind += 1

        res = ''
        max_len = max(self.count)
        new_ind = self.length - 1

        while new_ind >= 0:
            if self.count[new_ind] == max_len:
                res = str(self.seq[new_ind]) + ' ' + res
                max_len -= 1
            new_ind -= 1

        #print max(self.count)
        print res


def main():
    l = LS(10, [6, 1, 5, 3, 7, 1, 2, 5, 7, 4])
    k = LS(6, [5, 3, 4, 8, 6, 7])
    z = LS(8, [5, 2, 8, 6, 3, 6, 9, 7])

    l.ls_DP()
    #l.ls()
    #k.ls()
    #z.ls()

if __name__ == '__main__':
    main()
