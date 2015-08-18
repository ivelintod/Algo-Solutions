class VitoshaRun:

    def __init__(self, num, start_end, map):
        self.num = num
        self.start_end = start_end
        self.map = map
        self.graph = {}
        self.shortest_dist = {}

    def construct_graph(self):
        graph_temp = []
        for i in range(self.num):
            for j in range(self.num):
                if i > 0:
                    graph_temp.append([(i - 1, j), abs(self.map[i][j] - self.map[i - 1][j]) + 1])
                if i > 0 and j > 0:
                    graph_temp.append([(i - 1, j - 1), abs(self.map[i][j] - self.map[i - 1][j - 1]) + 1])
                if i > 0 and j < self.num - 1:
                    graph_temp.append([(i - 1, j + 1), abs(self.map[i][j] - self.map[i - 1][j + 1]) + 1])
                if j > 0:
                    graph_temp.append([(i, j - 1), abs(self.map[i][j] - self.map[i][j - 1]) + 1])
                if j < self.num - 1:
                    graph_temp.append([(i, j + 1), abs(self.map[i][j] - self.map[i][j + 1]) + 1])
                if i < self.num - 1:
                    graph_temp.append([(i + 1, j), abs(self.map[i][j] - self.map[i + 1][j]) + 1])
                if i < self.num - 1 and j > 0:
                    graph_temp.append([(i + 1, j - 1), abs(self.map[i][j] - self.map[i + 1][j - 1]) + 1])
                if i < self.num - 1 and j < self.num - 1:
                    graph_temp.append([(i + 1, j + 1), abs(self.map[i][j] - self.map[i + 1][j + 1]) + 1])
                self.graph[(i, j)] = graph_temp
                graph_temp = []

    def vitosha_run(self):
        start = self.start_end[0]
        end = self.start_end[1]
        vertices = [(x, y) for x in range(self.num) for y in range(self.num)]
        self.graph[start].append([start, 0])
        print vertices
        initial_connections = self.graph[start]
        print initial_connections
        while len(self.graph[start]) != self.num**2:
            temp = []
            count = 0
            for conn in initial_connections:
                for i in range(len(self.graph[conn[0]])):
                    for j in range(len(self.graph[start])):
                        if self.graph[conn[0]][i][0] == self.graph[start][j][0] and conn[1] + self.graph[conn[0]][i][1] < self.graph[start][j][1]:
                            self.graph[start][j][1] = conn[1] + self.graph[conn[0]][i][1]
                            count += 1
                        elif self.graph[conn[0]][i][0] == self.graph[start][j][0]:
                            count += 1

                    if count == 0:
                        new_connection = self.graph[conn[0]][i]
                        new_connection[1] += conn[1]
                        self.graph[start].append(new_connection)
                        temp.append(new_connection)
                    count = 0
                print self.graph[start]
            initial_connections = temp


        return self.graph[start]

    def construct_graph2(self):
        graph_temp = []
        for i in range(self.num):
            for j in range(self.num):
                if i > 0:
                    graph_temp.append(((i - 1, j), abs(self.map[i][j] - self.map[i - 1][j]) + 1))
                if i > 0 and j > 0:
                    graph_temp.append(((i - 1, j - 1), abs(self.map[i][j] - self.map[i - 1][j - 1]) + 1))
                if i > 0 and j < self.num - 1:
                    graph_temp.append(((i - 1, j + 1), abs(self.map[i][j] - self.map[i - 1][j + 1]) + 1))
                if j > 0:
                    graph_temp.append(((i, j - 1), abs(self.map[i][j] - self.map[i][j - 1]) + 1))
                if j < self.num - 1:
                    graph_temp.append(((i, j + 1), abs(self.map[i][j] - self.map[i][j + 1]) + 1))
                if i < self.num - 1:
                    graph_temp.append(((i + 1, j), abs(self.map[i][j] - self.map[i + 1][j]) + 1))
                if i < self.num - 1 and j > 0:
                    graph_temp.append(((i + 1, j - 1), abs(self.map[i][j] - self.map[i + 1][j - 1]) + 1))
                if i < self.num - 1 and j < self.num - 1:
                    graph_temp.append(((i + 1, j + 1), abs(self.map[i][j] - self.map[i + 1][j + 1]) + 1))
                self.graph[(i, j)] = graph_temp
                graph_temp = []


    def vitosha_run2(self):
        current = self.start_end[0]
        target = self.start_end[1]
        unvisited = [(x, y) for x in range(self.num) for y in range(self.num)]
        for node in unvisited:
            self.shortest_dist[node] = 'inf'
        self.shortest_dist[current] = 0
        while self.shortest_dist[target] == 'inf':
            index = None
            min_el = None
            print unvisited
            print current
            unvisited.remove(current)
            for conn in range(len(self.graph[current])):
                if self.graph[current][conn][0] in unvisited:
                    min_el = self.graph[current][conn][1]
                    index = conn
                    break

            for conn in range(len(self.graph[current])):
                if self.graph[current][conn][0] in unvisited and self.graph[current][conn][1] < min_el:
                    min_el = self.graph[current][conn][1]
                    index = conn

            self.shortest_dist[self.graph[current][index][0]] = 0
            self.shortest_dist[self.graph[current][index][0]] += self.shortest_dist[current] + min_el

            #print current
            current = self.graph[current][index][0]




def main():
    v = VitoshaRun(6, [(0, 0), (5, 5)], [[5, 3, 1, 4, 6, 7], [8, 1, 5, 6, 3, 1], [9, 8, 5, 1, 5, 2],
                                         [0, 9, 1, 3, 5, 8], [5, 2, 5, 7, 1, 7], [9, 8, 1, 4, 3, 9]])
    v.construct_graph2()
    print v.graph
    #print v.vitosha_run()
    print v.vitosha_run2()

if __name__ == '__main__':
    main()
