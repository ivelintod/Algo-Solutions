class MergeSort:

    def __init__(self, sequence):
        self.sequence = sequence
        self.dc = []
        self.result = []

    def divideAndConquer(self, sequence):
        result = []
        if len(sequence) < 2:
            return sequence
        sequence_part1 = sequence[:len(sequence) // 2]
        sequence_part2 = sequence[len(sequence) // 2:]
        one = self.divideAndConquer(sequence_part1)
        two = self.divideAndConquer(sequence_part2)
        while len(one) > 0 or len(two) > 0:
            if len(one) > 0 and len(two) > 0:
                if one[0] < two[0]:
                    result.append(one[0])
                    one.pop(0)
                else:
                    result.append(two[0])
                    two.pop(0)
            elif len(one) > 0:
                for i in one:
                    result.append(i)
                    one.pop(0)
            else:
                for j in two:
                    result.append(j)
                    two.pop(0)
        return result




def main():
    m = MergeSort([92, 34, 67, 43, 78, 65, 43, 3])
    print(m.divideAndConquer(m.sequence))


if __name__ == '__main__':
    main()
