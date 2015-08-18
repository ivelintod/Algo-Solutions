class DNA:

    def __init__(self, num, seq):
        self.num = num
        self.seq = seq
        self.graph = {}

    def make_graph(self):
        for nuc in self.seq:
            self.graph[nuc[:3]] = []
            self.graph[nuc[len(nuc) - 3:]] = []
        for nuc in self.seq:
            self.graph[nuc[:3]].append((nuc[len(nuc) - 3:], nuc[3:len(nuc) - 3]))
            self.graph[nuc[len(nuc) - 3:]].append((nuc[:3], nuc[3:len(nuc) - 3]))

    def uniform_span_tree(self):
        count = 0
        vertices = {x[:3] for x in self.seq}
        for x in self.seq:
            vertices.add(x[len(x) - 3:])
        vertices = list(vertices)
        odd_2_cycle = []
        for vertice in vertices:
            if len(self.graph[vertice]) % 2 != 0:
                count += 1
                odd_2_cycle.append(vertice)

        check_cycle = set()
        visited = []
        target_len = len(self.seq[0]) + (self.num - 1) * (len(self.seq[0][3:len(self.seq[0]) - 3]) + 3)

        if count == 0:
            start = vertices[0]
            result = start
            while len(result) != target_len:
                for conn in self.graph[start]:
                    if (start, conn[0]) not in visited:
                        result += conn[1] + conn[0]
                        visited.append((start, conn[0]))
                        visited.append((conn[0], start))
                        start = conn[0]
                        break
            print(result)

        elif count == 2:
            start = odd_2_cycle[0]
            result = start

            if len(self.graph[odd_2_cycle[0]]) == 1 and len(self.graph[odd_2_cycle[1]]) == 1:

                while len(result) != target_len - 8:
                    for conn in self.graph[start]:
                        if (start, conn[0]) not in visited:
                            if conn[0] != odd_2_cycle[1] and conn[0] not in check_cycle:
                                if conn[0] == self.graph[odd_2_cycle[1]][0][0]:
                                    check_cycle.add(conn[0])
                                result += conn[1] + conn[0]
                                visited.append((start, conn[0]))
                                visited.append((conn[0], start))
                                start = conn[0]
                                break

                for conn in self.graph[result[len(result) - 3:]]:
                    if conn[0] == self.graph[odd_2_cycle[1]][0]:
                        result += conn[1] + conn[0]
                for conn in self.graph[result[len(result) - 3:]]:
                    if conn[0] == odd_2_cycle[1]:
                        result += conn[1] + conn[0]
                print(result)
#TPFTASDJKEKLHUEWMLSALELGFOPUHUE
            else:

                while len(result) != target_len - 4:
                    for conn in self.graph[start]:
                        if (start, conn[0]) not in visited and conn[0] not in check_cycle:
                            if conn[0] == odd_2_cycle[1]:
                                check_cycle.add(conn[0])
                            result += conn[1] + conn[0]
                            visited.append((start, conn[0]))
                            visited.append((conn[0], start))
                            start = conn[0]
                            break

                for conn in self.graph[result[len(result) - 3:]]:
                    if conn[0] == odd_2_cycle[1]:
                        result += conn[1] + conn[0]
                print(result)

        else:
            print("IMPOSSIBLE")
            return


#TPFTASDGFFFJKEKLHUEFFFF
#HUEFASDGFFFJKEKLHUEWMLSALEL
#TPFTASDGFFFJKEKLHUEWMLSALELGFOPUHUE
#ASDGFFFJKEKLHUEUFOPGLELAMLSWHUEFASDTTPF
def main():
    d = DNA(9, ['FFFGASD', 'FFFJKEK', 'ASDFHUE', 'KEKLHUE', 'HUEWMLS', 'HUEUFOP', 'FOPGLEL', 'MLSALEL', 'ASDTTPF'])
    d.make_graph()
    print(d.graph)
    d.uniform_span_tree()


if __name__ == '__main__':
    main()



