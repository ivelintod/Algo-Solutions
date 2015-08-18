class Navigation:

    def __init__(self, N, M, S, C, junctions):
        self.N = N
        self.M = M
        self.start = S
        self.target = C
        self.junctions = junctions
        self.graph = {}
        self.graph2 = {}

    def final(self):
        for i in range(1, 9):
            self.graph[i] = 'inf'
        self.graph[self.start] = 0
        for i in range(1, 9):
            self.graph2[i] = []
        for junction in self.junctions:
            self.graph2[junction[0]].append((junction[1], junction[2]))
            self.graph2[junction[1]].append((junction[0], junction[2]))
        unvisited = [x for x in range(1, 9)]
        previous = []
        path = []
        current = self.start
        while self.graph[self.target] == 'inf':
            unvisited.remove(current)
            #previous.append(current)
            path.append(current)
            min_el = None
            index = None
            for s in range(len(self.graph2[current])):
                if self.graph2[current][s][0] in unvisited:
                    min_el = self.graph2[current][s][1]
                    index = s
            for s in range(len(self.graph2[current])):
                if self.graph2[current][s][0] in unvisited and self.graph2[current][s][1] < min_el:
                    min_el = self.graph2[current][s][1]
                    index = s

            self.graph[self.graph2[current][index][0]] = 0

            #for prev in previous:
            self.graph[self.graph2[current][index][0]] += self.graph[current]
            self.graph[self.graph2[current][index][0]] += min_el

            '''for conn in self.graph2[current]:
                if conn[0] == current and conn[1] < self.graph[self.graph2[current][index][0]]:
                    self.graph[self.graph2[current][index][0]] = conn[1]'''

            #previous.remove(current)
            current = self.graph2[current][index][0]
        path.append(self.target)

        print(self.graph[self.target])
        for previous in path:
            print(previous),
        print self.graph
        print self.graph2


def main():
    n = Navigation(8, 11, 1, 8, [(1, 2, 6), (1, 3, 2), (1, 4, 10), (2, 3, 3), (2, 4, 3),
                                 (2, 7, 8), (4, 6, 1), (6, 7, 2), (7, 5, 3), (7, 8, 12), (8, 5, 6)])
    #n.construct_graph()
    #print(n.graph)
    #n.navigate()
    n.final()


if __name__ == '__main__':
    main()
