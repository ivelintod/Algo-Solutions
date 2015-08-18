class HeapSort:

    def __init__(self, num, sequence):
        self.num = num
        self.sequence = sequence

    def order2(self, seq, left, right, i):
        if left > right:
            if left > seq[(i - 1) // 2]:
                seq[i - 1], seq[(i - 1) // 2] = seq[(i - 1) // 2], seq[i - 1]
                i = len(seq) - 1
                return i
        else:
            if right > seq[(i - 1) // 2]:
                seq[i], seq[(i - 1) // 2] = seq[(i - 1) // 2], seq[i]
                i = len(seq) - 1
                return i
        i -= 2
        return i

    def heapify2(self, seq):
        i = len(seq) - 1
        while i > 0:
            current = seq[i]
            if ((i - 1) // 2) == ((i - 2) // 2):
                left = seq[i - 1]
                right = current
                i = self.order2(seq, left, right, i)
            else:
                if current > seq[(i - 1) // 2]:
                    seq[i], seq[(i - 1) // 2] = seq[(i - 1) // 2], seq[i]
                    i = len(seq) - 1
                else:
                    i -= 1

        return seq

    def sort(self, seq):
        heap = self.heapify2(seq)
        res = heap
        for i in range(len(heap) - 1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0]
            if len(heap) > 0:
                res[i] = heap[len(heap) - 1]
            heap = self.heapify2(heap[:i])
        str_res = ''
        for r in res:
            str_res += str(r) + ' '

        print(str_res.strip(' '))


def main():
    num = int(input())
    seq_inp = input()
    seq = [int(x) for x in seq_inp.split()]
    h = HeapSort(num, seq)
    z = HeapSort(8, [10, 7, 20, 50, 70, 34, 3, 35, 21, 9, 43, 51, 19, 15])
    h.sort(h.sequence)


if __name__ == '__main__':
    main()
