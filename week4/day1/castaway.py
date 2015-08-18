class CastAway:

    GROUND = '#'
    SEA = '.'
    HARBOURS = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, dims, start_end, maps, H, harbours):
        self.dims = dims
        self.start_end = start_end
        self.map = maps
        self.H = H
        self.harbours = harbours
        self.res = list()
        self.visited = list()
        self.visited_harbours = list()
        self.graph = {}

    def check_island_harbours(self, x, y):
        forward = 1
        backward = 1
        consecutive = list()
        consecutive1 = list()

        if (x, y) not in self.visited:
            while True:
                if y + forward < self.dims[1]:
                    if self.map[x][y + forward] == CastAway.GROUND:
                        consecutive1.append((x, y + forward))
                        forward += 1
                    elif self.map[x][y + forward] in CastAway.HARBOURS:
                        if self.map[x][y + forward] not in self.res:
                            self.res.append(self.map[x][y + forward])
                        consecutive1.append((x, y + forward))
                        forward += 1
                    else:
                        break
                else:
                    break
            while True:
                if y - backward >= 0:
                    if self.map[x][y - backward] == CastAway.GROUND:
                        consecutive1.append((x, y - backward))
                        backward += 1
                    elif self.map[x][y - backward] in CastAway.HARBOURS:
                        if self.map[x][y - backward] not in self.res:
                            self.res.append(self.map[x][y - backward])
                        consecutive1.append((x, y - backward))
                        backward += 1
                    else:
                        break
                else:
                    break
            self.visited.append((x, y))

        for con in consecutive1:
            self.check_island_harbours(con[0], con[1])

        if x - 1 >= 0:
            if (x - 1, y) not in self.visited:
                if self.map[x - 1][y] == CastAway.GROUND:
                    consecutive.append((x - 1, y))
                elif self.map[x - 1][y] in CastAway.HARBOURS:
                    if self.map[x - 1][y] not in self.res:
                        self.res.append(self.map[x - 1][y])
                    consecutive.append((x - 1, y))

        if x + 1 < self.dims[0]:
            if (x + 1, y) not in self.visited:
                if self.map[x + 1][y] == CastAway.GROUND:
                    consecutive.append((x + 1, y))
                elif self.map[x + 1][y] in CastAway.HARBOURS:
                    if self.map[x + 1][y] not in self.res:
                        self.res.append(self.map[x + 1][y])
                    consecutive.append((x + 1, y))

        for cons in consecutive:
            self.check_island_harbours(cons[0], cons[1])

    def castaway(self, x, y):
        self.check_island_harbours(self.start_end[1][0], self.start_end[1][1])
        targets = list()
        harbours = list()
        for t in self.res:
            targets.append(t)
        print(targets)
        self.res = list()
        self.check_island_harbours(x, y)
        for h in self.res:
            harbours.append(h)
        print(harbours)
        queue = list()
        queue.append('start')
        queue.extend(harbours)
        #print queue
        self.res = list()
        index = 0
        for first in queue:
            self.graph[first] = [index, 1]
        while index < len(queue):
            for link in self.harbours:
                if queue[index] in link:
                    dest_temp = [x for x in link if x != queue[index] and x not in queue]
                    for d in dest_temp:
                        self.graph[d] = [index, 1]
                        if d in targets:
                            #print queue
                            break

                    queue += dest_temp

            for line in self.map:
                if queue[index] in line:
                    x = self.map.index(line)
                    y = line.index(queue[index])
                    self.check_island_harbours(x, y)
                    dest_temp = [j for j in self.res if j not in queue]
                    for d in dest_temp:
                        self.graph[d] = [index, 1]
                        if d in targets:
                            break

                    queue += dest_temp
                    self.res = list()

            index += 1

        count_days = 0
        res = list()
        for i in targets:
            if i in self.graph.keys():
                while True:
                    index = self.graph[i][0]
                    count_days += self.graph[i][1]
                    #print i
                    if index == 0:
                        res.append(count_days + 1)
                        break
                    i = queue[index]
            count_days = 0
        #print queue
        #print self.graph
        return min(res)


def main():
    '''dims_inp = input()
    start_end_inp = input()
    H_inp = input()
    harbours = list()
    dims = [int(x) for x in dims_inp.split()]
    start_end = [[int(x) for x in start_end_inp.split()[:2]], [int(x) for x in start_end_inp.split()[2:]]]'''

    with open('map.txt', 'r') as f:
        content = f.read()
        new_map = [[x for x in line.strip('\n')] for line in content.split(',')]

    '''H = int(H_inp)

    for i in range(H):
        harbours_inp = input()
        harbours.append([x for x in harbours_inp.split()])

    print(dims)
    print(start_end)
    print(new_map)
    print(harbours)

    #c = CastAway(dims, start_end, new_map, H, harbours)'''
    c = CastAway([14, 25], [[1, 9], [13, 24]], new_map, 9, [['a', 'e'], ['b', 'f'], ['c', 'b'], ['e', 'n'], ['m', 'g'],
                                                            ['n', 'h'], ['d', 'h'], ['h', 'l'], ['k', 'j']])
    #c.check_island_harbours(c.start_end[0][0], c.start_end[0][1])
    #print(c.res)
    print(c.castaway(c.start_end[0][0], c.start_end[0][1]))

if __name__ == '__main__':
    main()
