class KP:

    def __init__(self, num, edges, target):
        self.num = num
        self.edges = edges
        self.target = target
        self.visited = list()
        self.visited_paths = list()
        self.count_paths = 0
        self.count_steps = 0

    def k_paths(self):
        start = self.target[0]
        end = self.target[1]
        K = self.target[2]
        vertices = {x for junction in self.edges for x in junction}
        adj_matrix = [[0 for x in range(len(vertices))] for z in range(len(vertices))]
        for v in vertices:
            for junction in self.edges:
                if junction[0] == v:
                    adj_matrix[v][junction[1]] = 1
        print adj_matrix
        count_paths = 0
        count_steps = 0
        queue = list()
        queue.append(start)
        unvisited = set()
        res = []

        for i in range(len(adj_matrix[start])):
            if adj_matrix[start][i] == 1 and i != end:
                unvisited.add((start, i))

        while len(queue) > 0:
            #visited.add(queue[0])
            if adj_matrix[queue[0]][end] == 1 and count_steps == K - 1:
                count_paths = 1
                res.append(count_paths)
            else:
                for i in range(len(adj_matrix[queue[0]])):
                    if adj_matrix[queue[0]][i] == 1 and i != end and (queue[0], i) not in visited:
                        queue.append(i)

            count_steps += 1
            queue.pop(0)

            if count_paths != 0:
                queue = list()
                queue.append(start)
                count_paths = 0
                count_steps = 0

        print visited
        print sum(res)


    def build_matrix(self):
        #start = self.target[0]
        #end = self.target[1]
        #K = self.target[2]
        vertices = {x for junction in self.edges for x in junction}
        adj_matrix = [[0 for x in range(len(vertices))] for z in range(len(vertices))]
        for v in vertices:
            for junction in self.edges:
                if junction[0] == v:
                    adj_matrix[v][junction[1]] = 1
        return adj_matrix


    def paths(self, start, matrix):
        #self.visited.append(start)

        if start != self.target[0]:
            self.count_steps += 1

        if self.count_steps > self.target[2]:
            return

        #if matrix[start][self.target[1]] == 1 and start != self.target[0] and self.count_steps == self.target[2] - 1:
        if matrix[start][self.target[1]] == 1 and self.count_steps == self.target[2] - 1:
            self.count_paths += 1
            self.count_steps -= 1

        else:
            children = list()
            for i in range(len(matrix[start])):
                if matrix[start][i] == 1:
                    children.append(i)

            if len(children) == 0:
                #self.visited = self.visited[:len(self.visited) - 1]
                self.count_steps -= 1

            else:
                for child in children:
                    self.paths(child, matrix)
                #self.visited = self.visited[:len(self.visited) - 1]
                self.count_steps -= 1


def main():
    k = KP(5, [(0, 1), (1, 2), (0, 2), (1, 4), (0, 3), (1, 3), (2, 3), (0, 4), (4, 3)], (0, 3, 3))
    #k.k_paths()
    matrix = k.build_matrix()
    print matrix
    k.paths(k.target[0], matrix)
    print k.visited
    print k.visited_paths
    print k.count_paths

if __name__ == '__main__':
    main()
