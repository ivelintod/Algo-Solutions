class BP:

    def __init__(self, num_of_pr, projects, choice, dependencies):
        self.num_of_pr = num_of_pr
        self.choice = choice
        self.projects = projects
        self.dependencies = dependencies
        self.graph = {}
        self.visited = []
        self.visited2 = set()
        self.count = 1
        self.succession = 0
        self.build_order = []
        self.dependencies2 = {}
        for i in range(self.num_of_pr):
            self.dependencies2[self.projects[i]] = self.dependencies[i][1:]

    def construct_graph(self):
        for i in range(self.num_of_pr):
            self.graph[self.projects[i]] = i + 1
        return self.graph

    def construct_adjacency_matrix(self):
        matrix = [[0 for i in range(self.num_of_pr)] for i in range(self.num_of_pr)]
        for j in range(self.num_of_pr):
            k = 0
            if self.dependencies[j][0] != 0:
                for i in self.dependencies[j][1:]:
                    k += 1
                    matrix[j][self.graph[i] - 1] = k
        return matrix

    def construct_adjacency_matrix_for_validity(self):
        #self.construct_graph()
        matrix = [[0 for i in range(self.num_of_pr)] for i in range(self.num_of_pr)]
        for j in range(self.num_of_pr):
            if self.dependencies[j][0] != 0:
                for i in self.dependencies[j][1:]:
                    matrix[j][self.graph[i] - 1] = 1
        return matrix

    def check_graph(self, graph, start=0):
        children = list()
        flag = 'true'
        length = len(graph[0])
        self.visited.append(start)
        for i in range(length):
            if graph[start][i] == 1:
                if i in self.visited:
                    return 'false'
                children.append(i)

        if len(children) == 0:
            self.visited = self.visited[:len(self.visited) - 1]
        else:
            for child in children:
                flag = self.check_graph(graph, child)
                if flag is 'false':
                    break
            self.visited = self.visited[:len(self.visited) - 1]
        return flag

    def check_validity(self):
        matrix = self.construct_adjacency_matrix_for_validity()
        for i in range(len(matrix)):
            if self.check_graph(matrix, i) == 'false':
                return 'false'
            self.visited = []
        return 'true'

    def build(self, start, matrix):
        queue = list()
        index = 0
        if start not in self.visited2:
            while index < len(matrix[self.graph[start] - 1]):
                if matrix[self.graph[start] - 1][index] == 1:
                    queue.append(index)
                    for el in range(len(matrix[self.graph[start] - 1])):
                        if matrix[self.graph[start] - 1][el] != 0:
                            matrix[self.graph[start] - 1][el] -= 1
                    index = 0
                else:
                    index += 1
            self.visited2.add(start)
            if queue == list():
                if start not in self.build_order:
                    self.build_order.add(start)
                return self.build_order
            for el in queue:
                self.build_order = self.build(self.projects[el], matrix)
            if start not in self.build_order:
                self.build_order.add(start)

        return self.build_order

    def build2(self, start):
        self.visited2.add(start)
        for order in self.dependencies2[start]:
            if order not in self.visited2:
                self.build2(order)
        self.build_order.append(start)
        return self.build_order


def main():
    b = BP(5, ["Extensions", "Interface", "Core", "Common", "Networking"],"Interface",
        [[3, "Common", "Core", "Networking"], [4, "Core", "Common", "Extensions", "Networking"],
         [0], [1, "Core"], [2, "Core", "Common"]])
    #print(b.construct_adjacency_matrix())
    #print(b.construct_graph())
    #print(b.check_validity())
    b.construct_graph()
    print b.graph
    print b.check_validity()
    if b.check_validity() == 'false':
     print("BUILD ERROR")
    else:
     #matrix = b.construct_adjacency_matrix()
     #print(b.build(b.choice, matrix))
     print(b.build2(b.choice))

if __name__ == '__main__':
    main()
