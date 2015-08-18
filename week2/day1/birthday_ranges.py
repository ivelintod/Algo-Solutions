class BirthdayRanges:

    def __init__(self, birthdays, ranges):
        self.birthdays = birthdays
        self.ranges = ranges
        self.result = []

    def range(self):
        for r in self.ranges:
            left = r[0]
            right = r[1]
            count_birthdays = 0
            for b in self.birthdays:
                if b >= left and b <= right:
                    count_birthdays += 1
            self.result.append(count_birthdays)

        return self.result

    def count_sort(self):
        count_birthdays = [0] * 366

        for i in range(len(self.birthdays)):
            value = self.birthdays[i]
            count_birthdays[value] += 1

        for i in range(1, len(count_birthdays)):
            count_birthdays[i] += count_birthdays[i - 1]

        for r in self.ranges:
            res = count_birthdays[r[1]] - count_birthdays[r[0] - 1]
            self.result.append(res)

        return self.result



def main():
    b = BirthdayRanges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
    #print(b.range())
    print(b.count_sort())

if __name__ == '__main__':
    main()

