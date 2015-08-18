class MB:

    def __init__(self, num, matrix):
        self.num = num
        self.matrix = matrix

    def count_banana(self):

        j = 0
        while j <= self.num - 1:

            i = self.num - 1

            while j <= self.num - 1 and j >= 0 and i <= self.num - 1 and i >= 0:

                if i + 1 < self.num and j - 1 >= 0:
                    possibility1 = self.matrix[i + 1][j]
                    possibility2 = self.matrix[i][j - 1]
                    if possibility1 > possibility2:
                        self.matrix[i][j] += possibility1
                    else:
                        self.matrix[i][j] += possibility2

                elif i + 1 < self.num:
                    self.matrix[i][j] += self.matrix[i + 1][j]

                elif j - 1 >= 0:
                    self.matrix[i][j] += self.matrix[i][j - 1]

                i -= 1

            j += 1

        for row in self.matrix:
            print row
        print self.matrix[0][self.num - 1]





def main():
    m = MB(5, [[9, 3, 4, 1, 5], [1, 7, 1, 9, 1], [4, 2, 1, 3, 4], [2, 1, 2, 2, 1], [1, 3, 2, 1, 7]])
    m.count_banana()
    #m.count_banana2()

if __name__ == '__main__':
    main()
