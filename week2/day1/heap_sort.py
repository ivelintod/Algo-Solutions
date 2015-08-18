class HeapSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def construct_heap(self, sequence):
        i = 1
        k = 1
        #count_last_root = 0
        temp = len(sequence)
        while True:
            if temp < 2**k:
                temp -= i
                i *= 2
                k += 1
            else:
                return temp
        #return count_last_root

    def make_heap(self, sequence):
        heap = []
        min_el = sequence[0]
        for i in range(len(sequence) - 1):
            if sequence[i] < min_el:
                min_el = sequence[i]


    def sort(self, sequence):
        pass


def main():
    h = HeapSort([4,3,2,10,4,5,3,5,7,6])
    print(h.construct_heap(h.sequence))
    #print(h.make_heap(h.sequence))

if __name__ == '__main__':
    main()
