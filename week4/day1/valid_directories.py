class ValidDirectories:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def check_validity3(self, start=0):
        flag = 'true'
        length = len(self.graph)
        self.visited.append(start)
        children = list()
        #print self.visited
        for i in range(length):
            if self.graph[start][i] == 1:
                if i in self.visited:
                    flag = 'false'
                    return flag
                children.append(i)

        if len(children) != 0:
            for child in children:
                flag = self.check_validity3(child)
                if flag is 'false':
                    break
            #self.visited = self.visited[:len(self.visited) - 1]
        return flag

    '''def check_validity3(self, start=0):
        #self.visited.append(start)
        j = start
        father = {}
        queue = list()
        children = list()
        length = len(self.graph[0])
        queue.append(start)
        index = 0
        flag = None
        while index < len(queue):
            self.visited.append(queue[index])
            for i in range(length):
                if self.graph[start][i] == 1:
                    flag = 'false'
                    return flag
                father[i] = start
                children.append(i)

            if len(children) == 0 and father[start] != j:
                self.visited = self.visited[:len(self.visited) - 1]
            else:
                pass

        return 'true' '''

    def check_graph_validity(self):
        for i in range(len(self.graph)):
            if self.check_validity3(start=i) == 'false':
                #return 'false'
                pass
            print self.check_validity3(start=i)
            self.visited = []
        return 'true'


def main():

    v = ValidDirectories([[0, 1, 0, 0, 0, 2], [0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    print(v.check_validity3())
    print(v.check_graph_validity())

    b = ValidDirectories([[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 1], [0, 0, 0, 0, 0]])
    #print(b.check_validity3())
    #print(b.check_graph_validity())

if __name__ == '__main__':
    main()
