class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def check_graph(self, start=0):
        flag = True
        children = list()
        self.visited.append(start)
        length = len(self.graph)
        for i in range(length):
            if self.graph[start][i] == 1:
                if i in self.visited:
                    flag = False
                    return flag
                children.append(i)

        if len(children) == 0:
            self.visited = self.visited[:len(self.visited) - 1]
        else:
            for child in children:
                flag = self.check_graph(child)
            self.visited = self.visited[:len(self.visited) - 1]
        return flag

    def check_validity(self):
        for i in range(len(self.graph)):
            if self.check_graph(i) == False:
                return False
        return True


def list_loop(n):
    a_list = list()
    for i in range(n):
        if i % 3 == 0:
            a_list.append(i)
    return a_list

def list_compr(n):
    return [i for i in range(n) if i % 3 == 0]

#def main():
 #   b = Graph([[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 0, 0, 0, 0],
  #                        [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]])
   # print(b.check_graph())
    #print(b.check_validity())

    import timeit
    print(timeit.Timer("list_loop()").timeit())
    print(timeit.Timer("list_compr()").timeit())

if __name__ == '__main__':
    n = 1000
    from timeit import Timer
    t = Timer(lambda: list_compr(n))
    print t.timeit()
