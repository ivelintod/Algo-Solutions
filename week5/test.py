class PS:

    def __init__(self, N, N_junctions):
        self.N = N
        self.N_junctions = N_junctions
        self.streets = set()
        self.visited = []
        self.graph = {}

    def min_length(self):
        vertices_set = {x for junction in self.N_junctions for x in junction[:2]}
        vertices = list(vertices_set)
        queue = list()
        queue.append(vertices[0])
        visited = list()
        cable_len = 0
        while len(queue) < len(vertices):
            res = list()
            for item in queue:
                connections = [(x, y) for j in self.N_junctions for x in j[:2] for y in j[2:] if x != item and item in j]

                for e in range(len(connections)):
                    if (item,connections[e][0]) not in visited:
                        min_el = connections[e][1]
                        index = e
                        break
                for e in range(1, len(connections)):
                    if connections[e][1] < min_el and (item, connections[e][0]) not in visited and (connections[e][0], item) not in visited:
                        min_el = connections[e][1]
                        index = e
                res.append((item, connections[index]))

            index = 0
            min_el = res[index][1][1]
            for e in range(1, len(res)):
                if res[e][1][1] < min_el:
                    min_el = res[e][1][1]
                    index = e

            visited.append((res[index][0], res[index][1][0]))
            visited.append((res[index][1][0], res[index][0]))
            queue.append(res[index][1][0])
            cable_len += min_el

        return cable_len

    def construct_graph2(self):
        vertices = {x for junction in self.N_junctions for x in junction[:2]}
        vertices = list(vertices)
        for vertice in vertices:
            self.graph[vertice] = []
        print self.graph
        for junction in self.N_junctions:
            self.graph[junction[0]].append(junction[1])
            self.graph[junction[1]].append(junction[0])
        return self.graph

    def construct_graph(self, visited):
        vertices = {x for junction in self.N_junctions for x in junction[:2]}
        vertices = list(vertices)
        for vertice in vertices:
            self.graph[vertice] = []
        for v in visited:
            self.graph[v[0]].append(v[1])
            self.graph[v[1]].append(v[0])

    def check_connections(self, x, y):
        visited = list()
        queue = list()
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

    def Krusk_alg(self):
        visited = list()
        vertices = {x for junction in self.N_junctions for x in junction[:2]}
        cable_len = 0
        while len(visited) < len(vertices) - 1:
            self.construct_graph(visited)
            print self.graph
            for i in range(len(self.N_junctions)):
                if (self.N_junctions[i][0], self.N_junctions[i][1]) not in visited: #and not self.check_connections(self.N_junctions[i][0], self.N_junctions[i][1]):
                    min_el = self.N_junctions[i][2]
                    index = i
                    break
            for i in range(len(self.N_junctions)):
                if self.N_junctions[i][2] < min_el and (self.N_junctions[i][0], self.N_junctions[i][1]) not in visited and not self.check_connections(self.N_junctions[i][0], self.N_junctions[i][1]):
                    min_el = self.N_junctions[i][2]
                    index = i
            cable_len += min_el
            visited.append((self.N_junctions[index][0], self.N_junctions[index][1]))
            print visited

        return cable_len






def main():
    p = PS(12, [[1, 2, 1100], [1, 3, 1400], [1, 4, 2000], [2, 4, 2000], [2, 5, 1300], [1, 6, 2600],
                [3, 5, 780], [5, 4, 1000], [3, 4, 900], [3, 6, 1300], [6, 7, 200], [4, 7, 800]])
    print(p.min_length())
    #print(p.construct_graph())
    #print(p.check_connections(3, 2))
    print(p.Krusk_alg())
    print(p.min_length())

    z = PS(11, [[1, 2, 5], [2, 3, 13], [1, 4, 17], [2, 4, 12], [2, 7, 8], [3, 7, 11],
                [3, 5, 6], [4, 6, 10], [4, 7, 8], [5, 7, 14], [6, 7, 4]])
    print(z.Krusk_alg())
    #print(z.min_length())

    #only Krusk_alg() is working spot on...

if __name__ == '__main__':
    main()
