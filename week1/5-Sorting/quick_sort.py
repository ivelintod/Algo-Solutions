class QuickSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def quick_sort(self, sequence):
        result = []
        if len(sequence) < 2:
            return sequence
        length = len(sequence)
        pivot = sequence.pop(length // 2)
        sequence.insert(length, pivot)
        i = 0
        for el in sequence:
            if sequence[i] > pivot:
                #temp = sequence.pop(sequence.index(sequence[i]))
                sequence.insert(length, sequence[i])
                del sequence[i]
            else:
                i += 1
        first_seq = self.quick_sort(sequence[:sequence.index(pivot)])
        second_seq = self.quick_sort(sequence[sequence.index(pivot) + 1:])
        for i in first_seq:
            result.append(i)
        result.append(pivot)
        for j in second_seq:
            result.append(j)
        return result




def main():
    q = QuickSort([8, 7, 6, 5, 4, 3, 2, 1, 5])
    print(q.quick_sort(q.sequence))

if __name__ == '__main__':
    main()
