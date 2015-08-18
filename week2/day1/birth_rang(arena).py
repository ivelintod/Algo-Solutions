class BirthdayRanges:

    def __init__(self, people, num, birthdays, ranges):
        self.people = people
        self.num = num
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
    ppl_ranges_inp = input()
    ppl_ranges = [int(x) for x in ppl_ranges_inp.split()]
    ppl = int(ppl_ranges[0])
    ranges = int(ppl_ranges[1])
    people_inp = input()
    people = [int(person) for person in people_inp.split()]
    temp = []
    for i in range(ranges):
        j = input()
        temp.append([int(x) for x in j.split()])




    b = BirthdayRanges(ppl, ranges, people, temp)

    for x in b.count_sort():
        print(x),

if __name__ == '__main__':
    main()
