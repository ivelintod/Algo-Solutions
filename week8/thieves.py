class Thieves:

    def __init__(self, details, items):
        self.details = details
        self.items = items
        self.index = [None] * (self.details[1] + 1)

    def valuable(self):
        ind = 0

        while ind < len(self.items):

            to_be_added = set()

            for i in range(1, len(self.index)):

                if self.items[ind][0] <= self.details[1]:

                    if self.index[i] == self.items[ind][1] and i == self.items[ind][0]:
                        if self.index[i * 2] != None:
                            if self.index[i * 2] < self.index[i] * 2:
                                self.index[i * 2] = self.index[i] * 2
                        else:
                            self.index[i * 2] = self.index[i] * 2


                    if i == self.items[ind][0]:
                        if self.index[i] != None and self.index[i] < self.items[ind][1]:
                            self.index[i] = self.items[ind][1]

                        elif self.index[i] == None:
                            self.index[i] = self.items[ind][1]


                    if i - self.items[ind][0] > 0 and i - self.items[ind][0] != self.items[ind][0]: #and self.index[self.items[ind][0]] == self.items[ind]  #and self.index[self.items[ind][0]] == self.items[ind][0]:
                        if self.index[i - self.items[ind][0]] != None and self.index[i] == None:
                            value = self.index[i - self.items[ind][0]] + self.items[ind][1]
                            to_be_added.add((i, value))

                        elif self.index[i - self.items[ind][0]] != None and self.index[i] != None:
                            if self.index[i] < self.index[i - self.items[ind][0]] + self.items[ind][1]:
                                to_be_added.add((i,self.index[i - self.items[ind][0]] + self.items[ind][1]))

            #print to_be_added
            for i in to_be_added:
                self.index[i[0]] = i[1]
            to_be_added = set()

            ind += 1

        print self.index[self.details[1]]


    def no_shit(self):

        matrix = [[None for i in range(self.details[1] + 1)] for i in range(self.details[0] + 1)]
        for i in range(self.details[0] + 1):
            for j in range(self.details[1] + 1):
                if i == 0:
                    matrix[i][j] = 0
                if j == 0:
                    matrix[i][j] = 0


def knapsack_01(capacity, items):
    prev_row = [0] * (capacity + 1)
    for weight, value in items:
        this_row = prev_row[:weight]
        for idx in range(weight, capacity + 1):
            this_row.append(max(prev_row[idx], prev_row[idx - weight] + value))
        prev_row = this_row

    return prev_row


def main():
    t = Thieves((5, 5), [[3, 5], [7, 100], [1, 1], [1, 1], [2, 3]])
    t.valuable()
    print(knapsack_01(t.details[1], t.items))

    z = Thieves((12, 5), [[3, 5], [7, 100], [1, 1], [1, 1], [2, 3], [3, 10], [2, 11], [1, 4], [1, 7], [5, 20], [1, 10], [2, 15]])
    z.valuable()
    print(knapsack_01(z.details[1], z.items))

    k = Thieves((4, 10), [[6, 30], [3, 14], [4, 16], [2, 9]])
    k.valuable()
    print(knapsack_01(k.details[1], k.items))

    f = Thieves((4, 5), [[2, 12], [1, 10], [3, 20], [2, 15]])
    f.valuable()
    print(knapsack_01(f.details[1], f.items))


if __name__ == '__main__':
    main()
