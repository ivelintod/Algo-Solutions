class LCF:

    def __init__(self, N, NxN, M, queries):
        self.N = N
        self.NxN = NxN
        self.M = M
        self.queries = queries
        self.graph = {}
        self.visited = []

    def check_connection(self, k, p):
        self.visited.append(k)
        if self.NxN[k][p] != 0:
            return True
        else:
            for i in range(len(self.NxN)):
                if i not in self.visited:
                    if self.NxN[k][i] != 0:
                        return self.check_connection(i, p)
        return False

    def construct_graph(self):
        for i in range(len(self.NxN)):
            for j in range(len(self.NxN)):
                if self.NxN[i][j] != 0:
                    self.graph[(i, j)] = self.NxN[i][j]

    def find_better_routes(self):
        count = 0
        obvoius_paths = self.graph.keys()
        print(obvoius_paths)
        for path in obvoius_paths:
            for path2 in obvoius_paths:
                if path[1] == path2[0]:
                    if path[0] == path2[1]:
                        pass
                    elif (path[0], path2[1]) not in self.graph:
                        self.graph[(path[0], path2[1])] = self.graph[path] + self.graph[path2]
                        count += 1
                    else:
                        if self.graph[path] + self.graph[path2] < self.graph[(path[0], path2[1])]:
                            self.graph[(path[0], path2[1])] = self.graph[path] + self.graph[path2]
                            count += 1
        if count > 0:
            self.find_better_routes()


    def low_costs(self):
        for i in self.queries:
            if (i[0], i[1]) in self.graph.keys():
                print(self.graph[(i[0], i[1])])
            else:
                print "NO WAY"

def main():
    l = LCF(8, [[0, 9, 0, 3, 2, 0, 0, 0], [0, 0, 7, 2, 0, 0, 9, 0], [7, 0, 0, 0, 0, 7, 7, 0], [0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 5, 0], [0, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0]], 9,
                [[0, 5], [3, 6], [6, 4], [3, 2], [5, 4], [5, 3], [7, 6], [4, 5], [2, 6]])

    print(l.check_connection(4, 5))
    l.construct_graph()
    print(l.graph)
    print(l.find_better_routes())
    print(l.graph)
    l.low_costs()

if __name__ == '__main__':
    main()
