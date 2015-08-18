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

    def construct_graph(self):
        for i in range(self.num_of_pr):
            self.graph[self.projects[i]] = i + 1
        return self.graph

    def check_graph(self, graph, start):
        children = list()
        flag = 'true'

        self.visited.append(start)

        for i in graph[start]:
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
        for i in range(self.num_of_pr):
            if self.check_graph(self.dependencies, self.projects[i]) == 'false':
                return 'false'
            self.visited = []
        return 'true'

    def build2(self, start):
        self.visited2.add(start)
        for order in self.dependencies[start]:
            if order not in self.visited2:
                self.build2(order)
        self.build_order.append(start)
        return self.build_order



def main():
    num = int(input())
    scripts_inp = input()
    scripts = [x for x in scripts_inp.split()]
    choice = input()
    res = {}
    for i in range(num):
        order = input()
        temp = [x for x in order.split()]
        #temp[0] = int(temp[0])
        res[scripts[i]] = temp[1:]

    try:
        b = BP(num, scripts, choice, res)
        b.construct_graph()

        if b.check_validity() == 'false':
            print('BUILD ERROR')
        else:
            print(' '.join(b.build2(b.choice)))

    except Exception as e:
        print('BUILD ERROR')



if __name__ == '__main__':
    main()
