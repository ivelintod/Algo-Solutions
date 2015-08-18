class PhoneBook:

    def __init__(self):
        self.dict = {}

    def lookup_names(self, phone_book, numbers):
        res = []
        for t in phone_book:
            self.dict[t[0]] = t[1]
        for num in numbers:
            res.append(self.dict[num])
        for r in res:
            print(r)



def main():
    len_nums_inp = input()
    len_nums = [int(x) for x in len_nums_inp.split()]
    lens = len_nums[0]
    nums = len_nums[1]
    temp = []
    for i in range(lens):
        j = input()
        z = [x for x in j.split()]
        temp.append((int(z[0]), z[1]))
    temp2 = []
    for i in range(nums):
        p = input()
        temp2.append(int(p))

    p = PhoneBook()
    p.lookup_names(temp, temp2)

if __name__ == '__main__':
    main()
