class ClosestCoffeeStore:

    def __init__(self, num, graph, starting_point, is_coffee_store):
        self.num = num
        self.graph = graph
        self.starting_point = starting_point
        self.is_coffee_store = is_coffee_store
        self.visited = []

#BFS
    def closest_coffee_store2(self, graph, store, start):
        length = len(graph[start])
        q = list()
        q.append(start)
        i = 0
        while i < len(q):
            if store[q[i]] == 1:
                return q[i]
            self.visited.append(q[i])
            for j in range(length):
                if graph[q[i]][j] == 1 and store[j] == 1:
                    #print(j)
                    return j
                elif graph[q[i]][j] == 1 and j not in self.visited:
                    q.append(j)
            i += 1
        return -1


def main():
    num = int(input())
    temp = []
    for i in range(num):
        j = input()
        temp.append([int(x) for x in j.split()])
    start = int(input())
    c_stores_inp = input()
    c_stores = [int(x) for x in c_stores_inp.split()]

    c = ClosestCoffeeStore(num, temp, start, c_stores)

    print(c.closest_coffee_store2(c.graph, c.is_coffee_store, c.starting_point))


if __name__ == '__main__':
    main()
