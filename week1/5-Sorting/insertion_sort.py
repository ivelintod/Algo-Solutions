class InsertionSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def insertion_sort(self):
        for i in range(len(self.sequence) - 1):
            current = self.sequence[i + 1]
            ranged = self.sequence[:i + 1]
            diff = 0
            for j in ranged:
                if current < j:
                    diff += 1
            current = self.sequence.pop(i + 1)
            self.sequence.insert(i + 1 - diff, current)

        return self.sequence


def main():
    i = InsertionSort([92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10])
    print(i.insertion_sort())


if __name__ == '__main__':
    main()
