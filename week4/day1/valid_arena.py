class ValidDirectories:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def check_validity3(self, start=3):
        flag = 'false'
        length = len(self.graph)
        self.visited.append(start)
        children = list()
        for i in range(length):
            if self.graph[start][i] == 1:
                if i in self.visited or i == start:
                    flag = 'false'
                    return flag
                children.append(i)

        if len(children) != 0:
            for child in children:
                flag = self.check_validity3(child)
                if flag is 'false':
                    break
            self.visited = self.visited[:len(self.visited) - 1]
        return flag

    def check_graph_validity(self):
        for i in range(len(self.graph)):
            if self.check_validity3(start=i) == 'false' or self.graph[i][i] != 0:
                return 'false'
            self.visited = []
        return 'true'

def main():

    num = int(input())
    temp = []
    for i in range(num):
        j = input()
        temp.append([int(x) for x in j.split()])
    v = ValidDirectories(temp)
    print(v.check_graph_validity())

if __name__ == '__main__':
    main()
