class PS:

    def __init__(self, N, N_junctions):
        self.N = N
        self.N_junctions = N_junctions
        self.streets = set()
        self.graph = {}

    def construct_graph(self):
        for junction in self.N_junctions:
            self.streets.add(junction[0])
            self.streets.add(junction[1])
        for i in self.streets:
            self.graph[i] = []
            for junction in self.N_junctions:
                if i in junction:
                    self.graph[i].append([x for x in junction if x != i])
        return self.graph

    def find_min_weight(self):
        visited = list()
        cable_length = 0
        queue = list()
        self.construct_graph()
        streets = list(self.streets)
        print streets
        start = streets[0]
        queue.append(start)
        while len(queue) < len(streets):
            res = []
            for item in queue:
                for j in range(len(self.graph[item])):
                    if (item, self.graph[item][j][0]) not in visited:
                        min_el = self.graph[item][j][1]
                        index = j
                        break
                for j in range(1, len(self.graph[item])):
                    if (item, self.graph[item][j][0]) not in visited:
                        if self.graph[item][j][1] < min_el:
                            min_el = self.graph[item][j][1]
                            index = j
                res.append(self.graph[item][index])

            min_el = res[0][1]
            index = 0
            for i in range(1, len(res)):
                if res[i][1] < min_el:
                    min_el = res[i][1]
                    index = i
            if (item, res[index][0]) not in visited:
                cable_length += min_el
                visited.append((item, res[index][0]))
                visited.append((res[index][0], item))
                queue.append(res[index][0])
        print visited
        print self.graph
        return cable_length

    def find_min_weight2(self):
        single_headed = {x for y in self.N_junctions for x in y[:len(y) - 1]}
        single_headed_trees = [[x] for x in single_headed]
        print(single_headed_trees)
        edges = [x for y in self.N_junctions for x in y[len(y) - 1:]]
        print(edges)
        res = []
        cable_length = 0
        while len(edges) != 0 and len(single_headed_trees) > 1:
            index = 0
            min_edge = edges[index]
            for e in range(1, len(edges)):
                if edges[e] < min_edge:
                    index = e
            min_edge = edges.pop(index)
            for junction in self.N_junctions:
                if min_edge in junction:
                    for t in range(len(single_headed_trees)):
                        if junction[0] in single_headed_trees[t] and junction[1] not in single_headed_trees[t]:
                            single_headed_trees[t] += [junction[1]]
                            single_headed_trees.remove([junction[1]])
                            cable_length += min_edge
                            break
        print single_headed_trees
        print edges
        print res

    def find_min_length(self):
        single_headed = {x for y in self.N_junctions for x in y[:len(y) - 1]}
        single_headed_trees = [[x] for x in single_headed]
        print(single_headed_trees)
        edges = [x for y in self.N_junctions for x in y[len(y) - 1:]]
        print(edges)
        res = list()
        cable_length = 1
        count_edges = 0
        connected = list()
        while count_edges < len(single_headed_trees) - 1:
            index = 0
            min_edge = edges[index]
            for e in range(1, len(edges)):
                if edges[e] < min_edge:
                    min_edge = edges[e]
                    index = e
            min_edge = edges.pop(index)
            print min_edge
            for junction in self.N_junctions:
                if min_edge in junction and junction[0] not in res and junction[1] not in res:
                    res.append(junction[0])
                    res.append(junction[1])
                    connected.append((junction[0], junction[1]))
                    cable_length += min_edge
                    count_edges += 1
                    print count_edges
                elif min_edge in junction and (junction[0], junction[1]) not in connected:
                    connected.append((junction[0], junction[1]))
                    cable_length += min_edge
                    count_edges += 1
                elif min_edge in junction and junction[0] not in res:
                    res.append(junction[0])
                    cable_length += min_edge
                    count_edges += 1
                    print count_edges
                elif min_edge in junction and junction[1] not in res:
                    res.append(junction[1])
                    cable_length += min_edge
                    count_edges += 1
                    print count_edges
        print res
        return cable_length


def main():
    p = PS(12, [[1, 2, 1100], [1, 3, 1400], [1, 4, 2000], [2, 4, 2000], [2, 5, 1300], [1, 6, 2600],
                [3, 5, 780], [5, 4, 1000], [3, 4, 900], [3, 6, 1300], [6, 7, 200], [4, 7, 800]])
    print(p.find_min_weight())

    z = PS(11, [[1, 2, 5], [2, 3, 13], [1, 4, 17], [2, 4, 12], [2, 7, 8], [3, 7, 11],
                [3, 5, 6], [4, 6, 10], [4, 7, 8], [5, 7, 14], [6, 7, 4]])
    print(z.find_min_weight())
    #print(p.construct_graph())
    #print(p.find_min_weight2())
    #print(p.find_min_length())



if __name__ == '__main__':
    main()
