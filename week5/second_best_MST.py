class SBMST:

    def __init__(self, N, N_junctions):
        self.N = N
        self.N_junctions = N_junctions
        self.def_graph = {}
        self.graph = {}
        self.visited = []
        self.vertices = list({x for junction in self.N_junctions for x in junction[:2]})

    def construct_default_graph(self):
        for vertice in self.vertices:
            self.def_graph[vertice] = []
        for junction in self.N_junctions:
            self.def_graph[junction[0]].append(junction[1])
            self.def_graph[junction[1]].append(junction[0])
        print self.def_graph

    def construct_graph(self, visited):
        for vertice in self.vertices:
            self.graph[vertice] = []
        for v in visited:
            self.graph[v[0]].append(v[1])
            self.graph[v[1]].append(v[0])

    def check_connections(self, x, y):
        visited = []
        queue = []
        queue.append(x)
        index = 0
        while index < len(queue):
            visited.append(queue[index])
            for kid in self.graph[queue[index]]:
                if kid not in visited:
                    if y in self.graph[kid]:
                        return True
                    queue.append(kid)
            index += 1
        return False


    def MST(self):
        visited = []
        cable_len = 0
        while len(visited) < len(self.vertices) - 1:
            self.construct_graph(visited)
            for j in range(len(self.N_junctions)):
                if (self.N_junctions[j][0], self.N_junctions[j][1]) not in visited and not self.check_connections(self.N_junctions[j][0], self.N_junctions[j][1]):
                    min_el = self.N_junctions[j][2]
                    index = j

            for j in range(len(self.N_junctions)):
                if self.N_junctions[j][2] < min_el and (self.N_junctions[j][0], self.N_junctions[j][1]) not in visited and not self.check_connections(self.N_junctions[j][0], self.N_junctions[j][1]):
                    min_el = self.N_junctions[j][2]
                    index = j

            cable_len += min_el
            visited.append((self.N_junctions[index][0], self.N_junctions[index][1]))

        #print visited
        self.construct_graph(visited)
        #print self.graph
        #return cable_len
        return (visited, cable_len)

    def temporary_partial_ST(self, visited):
        pass

    def second(self):
        visited = self.MST()[0]
        print visited
        index = 0
        self.construct_default_graph()
        res = []
        while index < len(visited):
            temp = visited[index]
            for i in range(len(visited[index])):
                for vertice in self.def_graph[visited[index][i]]:
                    visited.remove(temp)
                    self.construct_graph(visited)
                    if i == 0:
                        if vertice != temp[i + 1]:
                            if not self.check_connections(temp[i], vertice) and (temp[i], vertice) not in visited and (vertice, temp[i]) not in visited:
                                current = [x for junction in self.N_junctions for x in junction[2:] if temp[0] in junction[:2] and temp[1] in junction[:2]][0]
                                candidate = [x for junction in self.N_junctions for x in junction[2:] if temp[i] in junction[:2] and vertice in junction[:2]][0]
                                res.append((current, candidate))

                    if i == 1:
                        if vertice != temp[i - 1]:
                            if not self.check_connections(temp[i], vertice) and (temp[i], vertice) not in visited and (vertice, temp[i]) not in visited:
                                current = [x for junction in self.N_junctions for x in junction[2:] if temp[0] in junction[:2] and temp[1] in junction[:2]][0]
                                candidate = [x for junction in self.N_junctions for x in junction[2:] if temp[i] in junction[:2] and vertice in junction[:2]][0]
                                res.append((current, candidate))
                    visited.insert(index, temp)
            index += 1
        print res
        vertice_diff = [res[i][1] - res[i][0] for i in range(len(res))]
        second_best_length = self.MST()[1] + min(vertice_diff)
        return second_best_length





def main():
    s = SBMST(11, [[1, 2, 5], [2, 3, 13], [1, 4, 17], [2, 4, 12], [2, 7, 8], [3, 7, 11],
                   [3, 5, 6], [4, 6, 10], [4, 7, 8], [5, 7, 14], [6, 7, 4]])

    #print(s.MST())
    #print(s.second_best())
    #s.construct_default_graph()
    print(s.second())

if __name__ == '__main__':
    main()
