class BR:

    def __init__(self, junc_str, junctions, BPH):
        self.junc_str = junc_str
        self.junctions = junctions
        self.BPH = BPH

    def find_shortest_path_BH(self):
        default_matrix = [['inf' for i in range(self.junc_str[0] + 1)] for j in range(self.junc_str[0] + 1)]
        for junc in self.junctions:
            default_matrix[junc[0]][junc[1]] = 1
            default_matrix[junc[1]][junc[0]] = 1

        print default_matrix

        matrix = [['inf' for i in range(self.junc_str[0] + 1)] for j in range(self.junc_str[0] + 1)]
        for i in range(self.junc_str[0] + 1):
            for j in range(self.junc_str[0] + 1):
                if i == j:
                    matrix[i][j] = 0
                if default_matrix[i][j] == 1:
                    matrix[i][j] = 1
                    for k in range(i):
                        if matrix[k][i] != 'inf' and matrix[k][j] == 'inf':
                            matrix[k][j] = matrix[k][i] + 1
                        elif matrix[k][i] != 'inf' and matrix[k][j] > matrix[k][i] + 1:
                            matrix[k][j] = matrix[k][i] + 1

        print matrix

        if matrix[self.BPH[1]][self.BPH[2]] < matrix[self.BPH[0]][self.BPH[2]]:
            return 0
        else:
            return matrix[self.BPH[1]][self.BPH[2]] - matrix[self.BPH[0]][self.BPH[2]] - 1


def main():
    b = BR((11, 15), [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (4, 7), (5, 7),
                            (6, 9), (6, 9), (7, 9), (7, 10), (8, 9), (9, 10), (10, 11)], (8, 1, 11))

    print(b.find_shortest_path_BH())

if __name__ == '__main__':
    main()
