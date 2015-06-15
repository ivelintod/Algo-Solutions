class CountSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def count_sort(self, sequence):
        max_el = sequence[0]
        for el in sequence:
            if el > max_el:
                max_el = el

        count_list = [0] * (max_el + 1)
        for el in sequence:
            count_list[el] += 1

        for i in range(len(count_list) - 1):
            count_list[i + 1] += count_list[i]

        result = [None] * len(sequence)
        length = len(result) - 1
        while length >= 0:
            count_index = sequence[length]
            count_list[count_index] -= 1
            value = count_list[count_index]
            result[value] = sequence[length]
            length -= 1

        return result





def main():

    c = CountSort([2, 8, 7, 6, 5, 4, 3, 2])
    print(c.count_sort(c.sequence))


if __name__ == '__main__':
    main()

