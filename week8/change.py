class Change:

    def __init__(self, target):
        self.target = target
        self.index = [0] * (self.target + 1)
        self.coins = [2, 5, 10, 20, 50, 100]
        self.index[0] = 0

    def count_change(self):
        ind = 0
        while ind < len(self.coins):

            for i in range(1, self.target + 1):
                if i == self.coins[ind]:
                    self.index[i] += 1

                #for j in self.coins[ind:ind + 1]:
                if i - self.coins[ind] > 0:
                    self.index[i] += self.index[i - self.coins[ind]]

            ind += 1

        print(self.index)

#Extra task (working only for coins [1, 2, 5, 10, 20, 50, 100])

    def count_min_coins(self):
        ind = 0
        while ind < len(self.coins):

            for i in range(1, self.target + 1):
                if i == self.coins[ind]:
                    self.index[i] = 1

                elif ind == 0:
                    self.index[i] += self.index[i - 1] + 1

                else:
                    if i - self.coins[ind] > 0:
                        #if self.index[i] > self.index[i - self.coins[ind]] + 1:
                        self.index[i] = self.index[i - self.coins[ind]] + 1

            ind += 1
        print(self.index)

#Extra task (working for universal coins).......

    def count_min_coins2(self):
        ind = 0
        while ind < len(self.coins):

            temp_sum = self.coins[ind]
            for i in range(1, self.target + 1):
                if i == self.coins[ind]:
                    self.index[i] = 1

                if ind == 0:
                    if i == self.coins[ind] + temp_sum:
                        self.index[i] = self.index[temp_sum] + 1
                        temp_sum = i
                else:
                    if i - self.coins[ind] > 0:
                        if self.index[i - self.coins[ind]] != 0:
                            self.index[i]  = self.index[i - self.coins[ind]] + 1

            ind += 1

        print self.index


def main():
    c = Change(25)
    #c.count_change()
    #c.count_min_coins()
    c.count_min_coins2()

if __name__ == '__main__':
    main()
