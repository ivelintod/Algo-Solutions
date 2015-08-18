class ClosestCoffeeStore:

    def __init__(self, graph, is_coffee_store, starting_point):
        self.graph = graph
        self.is_coffee_store = is_coffee_store
        self.starting_point = starting_point
        self.visited = []

#DFS
    def closest_coffee_store(self, graph, store, start):
        length = len(graph[start])
        for i in range(length):
            if graph[start][i] == 1 and store[i] == 1:
                return i
        else:
            for i in range(length):
                self.visited.append(start)
                if graph[start][i] == 1 and i not in self.visited:
                    return self.closest_coffee_store(graph, store, i)
        return -1

#BFS
    def closest_coffee_store2(self, graph, store, start):
        length = len(graph[start])
        q = list()
        q.append(start)
        i = 0
        while i < len(q):
            if store[q[i]] == 1:
                print q[i]
                return
            self.visited.append(q[i])
            for j in range(length):
                if graph[q[i]][j] == 1 and store[j] == 1:
                    print j
                    return
                elif graph[q[i]][j] == 1 and j not in self.visited:
                    q.append(j)
            i += 1
        print -1


def main():

    c = ClosestCoffeeStore([[0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]],
                           [1, 0, 0, 0, 0, 0], 0)
    #print(c.closest_coffee_store(c.graph, c.is_coffee_store, c.starting_point))
    c.closest_coffee_store2(c.graph, c.is_coffee_store, c.starting_point)

if __name__ == '__main__':
    main()
