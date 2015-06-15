class SelectionSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def selection_sort(self):
        for i in range(len(self.sequence)):
            min_el = min(self.sequence[i:])
            temp = self.sequence[i]
            j = self.sequence[i:].index(min_el) + i
            self.sequence[i] = min_el
            self.sequence[j] = temp
        return self.sequence


def main():
    s = SelectionSort([92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10])
    print(s.selection_sort())


if __name__ == '__main__':
    main()
