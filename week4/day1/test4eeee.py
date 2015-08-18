class BP:

    def __init__(self, num_of_pr, projects, choice, dependencies):
        self.num_of_pr = num_of_pr
        self.choice = choice
        self.projects = projects
        self.dependencies = dependencies
        self.graph = {}
        self.visited = []
        self.count = 1
        self.succession = 0
        self.build_order = []
        self.dependencies2 = []
        for dep in self.dependencies:
            self.dependencies2.append(dep[1:])

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
        matrix = [[0 for i in range(self.num_of_pr)] for i in range(self.num_of_pr)]
        for j in range(self.num_of_pr):
            if self.dependencies[j][0] != 0:
                for i in self.dependencies[j][1:]:
                    matrix[j][self.graph[i] - 1] = 1
        return matrix

    def check_graph(self, graph, start=0):
        children = list()
        flag = True
        length = len(graph[0])
        self.visited.append(start)
        for i in range(length):
            if graph[start][i] == 1:
                if i in self.visited:
                    return False
                children.append(i)

        if len(children) == 0:
            self.visited = self.visited[:len(self.visited) - 1]
        else:
            for child in children:
                flag = self.check_graph(graph, child)
                if flag is False:
                    break
            self.visited = self.visited[:len(self.visited) - 1]
        return flag

    def check_validity(self):
        matrix = self.construct_adjacency_matrix_for_validity()
        for i in range(len(matrix)):
            if self.check_graph(matrix, i) == False:
                return False
        return True

    def build2(self, start):
        self.visited2.append(start)
        for order in self.dependencies2[self.graph[start] - 1]:
            if order not in self.visited2:
                self.build2(order)
        self.build_order.append(start)
        return self.build_order



def main():
    '''num = int(input())
    scripts_inp = input()
    scripts = [x for x in scripts_inp.split()]
    choice = input()
    res = []
    for i in range(num):
        order = input()
        temp = [x for x in order.split()]
        temp[0] = int(temp[0])
        res.append(temp)
    try:
     b = BP(num, scripts, choice, res)
     b.construct_graph()
     if not b.check_validity():
      print('BUILD ERROR')
     else:
      for i in b.build2(b.choice):
       print(i, end =' ')
    except Exception as e:
     print('BUILD ERROR')'''

    a = set()
    for i in ['lq', 'b', 'weara']:
        a.add(i)
    for i in a:
        print i,

if __name__ == '__main__':
    main()
