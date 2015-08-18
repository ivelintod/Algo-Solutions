class HS:

    def __init__(self, seq):
        self.seq = seq
        self.seq.insert(0, None)
        self.heap_sorted = list()

    def heapify(self):
        #heap = []
        i = len(self.seq) - 1
        while i > 1:
            #parent = self.seq[i // 2]
            if i // 2 == (i - 1) // 2:
                if self.seq[i] < self.seq[i - 1]:
                    if self.seq[i] < self.seq[i // 2]:
                        self.seq[i], self.seq[i // 2] = self.seq[i // 2], self.seq[i]
                        self.check_order(i)
                else:
                    if self.seq[i - 1] < self.seq[i // 2]:
                        self.seq[i - 1], self.seq[i // 2] = self.seq[i // 2], self.seq[i - 1]
                        self.check_order(i - 1)
                i -= 2

            else:
                if self.seq[i] < self.seq[i // 2]:
                    self.seq[i], self.seq[i // 2] = self.seq[i // 2], self.seq[i]
                    self.check_order(i)
                i -= 1

        '''addition = self.seq.pop(1)
        self.heap_sorted.append(addition)
        while len(self.seq) != 1:
            self.heapify()'''

    def check_order(self, ind):
        while True:
            if ind * 2 + 1 < len(self.seq):
                if self.seq[ind * 2] < self.seq[ind * 2 + 1]:
                    if self.seq[ind * 2] < self.seq[ind]:
                        self.seq[ind], self.seq[ind * 2] = self.seq[ind * 2], self.seq[ind]
                        ind *= 2
                    else:
                        break
                else:
                    if self.seq[ind * 2 + 1] < self.seq[ind]:
                        self.seq[ind], self.seq[ind * 2 + 1] = self.seq[ind * 2 + 1], self.seq[ind]
                        ind = ind * 2 + 1
                    else:
                        break
            elif ind * 2 < len(self.seq):
                if self.seq[ind * 2] < self.seq[ind]:
                    self.seq[ind], self.seq[ind * 2] = self.seq[ind * 2], self.seq[ind]
                    ind *= 2
                else:
                    break
            else:
                break



    def pop_highest_priority(self):
        self.seq[1], self.seq[len(self.seq) - 1] = self.seq[len(self.seq) - 1], self.seq[1]
        highest_pr = self.seq[len(self.seq) - 1]
        del self.seq[len(self.seq) - 1]

        self.check_order(1)
        return highest_pr

    def heap_sort(self):
        self.heapify()
        sorted_seq = list()
        while len(self.seq) > 1:
            #print self.seq
            min_el = self.pop_highest_priority()
            sorted_seq.append(min_el)

        return sorted_seq




def main():
    num = int(input())
    seq_inp = input()
    seq = [int(x) for x in seq_inp.split()]

    h = HS(seq)
    #h.heapify()
    #print h.seq
    res = ''
    for s in h.heap_sort():
        res += ' ' + str(s)
    print(res.strip(' '))


if __name__ == '__main__':
    main()
#[6, 1, 5, 3, 9, 2, 5, 7]
