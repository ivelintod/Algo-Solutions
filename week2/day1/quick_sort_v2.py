class QuickSort:

    def __init__(self):
        pass

    def quick_sort(self, sequence):
        result = []
        length = len(sequence)
        if length < 2:
            return sequence
        pivot = sequence.pop(length/2)
        sequence.insert(length - 1, pivot)
        #print sequence
        count = 0
        i = 0
        for j in range(length):
            if sequence[i] > pivot:
                el = sequence.pop(i)
                sequence.insert(length - 1, el)
                count += 1
            else:
                i += 1
        left = self.quick_sort(sequence[:length - count -1])
        right = self.quick_sort(sequence[length - count:])
        for i in left:
            result.append(i)
        result.append(pivot)
        for j in right:
            result.append(j)
        return result




def main():
    q = QuickSort()
    print(q.quick_sort([8, 7, 7, 6, 5, 5, 4, 3, 2, 1, 5]))

if __name__ == '__main__':
    main()
