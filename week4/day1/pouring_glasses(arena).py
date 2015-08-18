class PG:

    def __init__(self, capacities, quantities, G):
        self.capacities = capacities
        self.quantities = quantities
        self.G = G
        self.visited = []
        self.graph = {}

    def pouring_glasses(self):
        start = self.quantities
        children = list()
        queue = list()
        res = list()
        index = 0
        tuple_start = tuple(start)
        queue.append(tuple_start)
        avail1 = self.capacities[0] - start[0]
        avail2 = self.capacities[1] - start[1]
        avail3 = self.capacities[2] - start[2]

        if self.G in self.quantities:
            print('IMPOSSIBLE')
            return

        while index < len(queue):
            avail1 = self.capacities[0] - queue[index][0]
            avail2 = self.capacities[1] - queue[index][1]
            avail3 = self.capacities[2] - queue[index][2]

            if queue[index] not in self.visited:
                for i in range(len(start)):

                    if i == 0:
                        if avail2 != 0:
                            if queue[index][i] >= avail2:
                                temp1 = queue[index][i] - avail2
                                temp2 = queue[index][i + 1] + avail2
                                temp3 = queue[index][i + 2]
                            else:
                                temp1 = 0
                                temp2 = queue[index][i + 1] + queue[index][i]
                                temp3 = queue[index][i + 2]
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(1, 2), index]


                        if avail3 != 0:
                            if queue[index][i] >= avail3:
                                temp1 = queue[index][i] - avail3
                                temp2 = queue[index][i + 1]
                                temp3 = queue[index][i + 2] + avail3

                            else:
                                temp1 = 0
                                temp2 = queue[index][i + 1]
                                temp3 = queue[index][i + 2] + queue[index][i]
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(1, 3), index]

                    if i == 1:
                        if avail1 != 0:
                            if queue[index][i] >= avail1:
                                temp1 = queue[index][i - 1] + avail1
                                temp2 = queue[index][i] - avail1
                                temp3 = queue[index][i + 1]

                            else:
                                temp1 = queue[index][i - 1] + queue[index][i]
                                temp2 = 0
                                temp3 = queue[index][i + 1]
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(2, 1), index]

                        if avail3 != 0:
                            if queue[index][i] >= avail3:
                                temp1 = queue[index][i - 1]
                                temp2 = queue[index][i] - avail3
                                temp3 = queue[index][i + 1] + avail3

                            else:
                                temp1 = queue[index][i - 1]
                                temp2 = 0
                                temp3 = queue[index][i + 1] + queue[index][i]
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(2, 3), index]

                    if i == 2:
                        if avail1 != 0:
                            if queue[index][i] >= avail1:
                                temp1 = queue[index][i - 2] + avail1
                                temp2 = queue[index][i - 1]
                                temp3 = queue[index][i] - avail1

                            else:
                                temp1 = queue[index][i - 2] + queue[index][i]
                                temp2 = queue[index][i - 1]
                                temp3 = 0
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(3, 1), index]

                        if avail2 != 0:
                            if queue[index][i] >= avail2:
                                temp1 = queue[index][i - 2]
                                temp2 = queue[index][i - 1] + avail2
                                temp3 = queue[index][i] - avail2

                            else:
                                temp1 = queue[index][i - 2]
                                temp2 = queue[index][i - 1] + queue[index][i]
                                temp3 = 0
                            if (temp1, temp2, temp3) not in queue:
                                children.append((temp1, temp2, temp3))
                                self.graph[(temp1, temp2, temp3)] = [(3, 2), index]

                self.visited.append(queue[index])

                for child in children:

                    if child[0] == self.G or child[1] == self.G or child[2] == self.G:
                        #return self.graph, queue
                        while True:
                            i = self.graph[child][1]
                            res.append(self.graph[child][0])
                            child = queue[i]
                            if i == 0:
                                print(len(res))
                                for j in res[::-1]:
                                    print(j[0]),
                                    print(j[1])
                                return


                    #if child not in self.visited:
                    queue.append(child)

            children = list()

            index += 1

        print('IMPOSSIBLE')


def main():
    availability = input()
    a = [int(x) for x in availability.split()]
    glasses = input()
    g = [int(x) for x in glasses.split()]
    target = input()
    t = int(target)
    p = PG(a, g, t)
    p.pouring_glasses()

if __name__ == '__main__':
    main()
