class Quadruplets:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def count_zero_Quadruplets(self, i=0):
        count = 0
        for a in self.a:
            for b in self.b:
                for c in self.c:
                    for d in self.d:
                        if a + b + c + d == 0:
                            count += 1
        return count

    def count_zero_quadruplets(self):
        #first = self.a + self.b
        #j = len(self.a)
        f_res = []
        s_res = []
        for a in self.a:
            for b in self.b:
                f_res.append(a + b)
        for c in self.c:
            for d in self.d:
                s_res.append(c + d)

        count = 0
        for f in f_res:
            for s in s_res:
                if f + s == 0:
                    print (f, s)
                    count += 1

        return count

    def count_0_quadruplets(self):
        pass




def main():
    q = Quadruplets([5, 3, 4], [-2, -1, 6], [-1, -2, 4], [-1, -2, 7])
    print(q.count_zero_Quadruplets())
    print(q.count_zero_quadruplets())

if __name__ == '__main__':
    main()
