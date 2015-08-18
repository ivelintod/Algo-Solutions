class PN:

    def __init__(self, num_of_students, phones_of_st, phone_details):
        self.num_of_students = num_of_students
        self.phones_of_st = phones_of_st
        self.phone_details = phone_details
        self.graph = {}
        self.num_to_student = {}
        self.visited = []

    def construct_graph(self):
        for i in range(self.num_of_students):
            if self.phone_details[i][0] != 0:
                self.graph[i + 1] = [x for x in self.phone_details[i][1:]]
            else:
                self.graph[i + 1] = None
        return self.graph

    def make_num_to_student(self):
        for i in range(self.num_of_students):
            self.num_to_student[self.phones_of_st[i]] = i + 1

    def find_min_calls(self):
        calls = 0
        for i in range(self.num_of_students):
            if self.graph[i + 1] == None:
                calls += 1
                self.visited.append(i + 1)
        student = 1
        count_add = 0

        while True:
            if len(self.visited) == self.num_of_students:
                break
            if self.graph[student] is not None:
                for num in self.graph[student]:
                    if self.num_to_student[num] not in self.visited:
                        self.visited.append(self.num_to_student[num])
                        count_add += 1
                if count_add > 0:
                    calls += 1
                    self.visited.append(student)
                student += 1
                count_add = 0
            else:
                student += 1

        return calls

def main():
    num = int(input())
    numbers_inp = input()
    temp = []
    for i in range(num):
        j = input()
        temp.append([int(x) for x in j.split()])
    numbers = [int(x) for x in numbers_inp.split()]

    p = PN(num, numbers, temp)
    p.construct_graph()
    p.make_num_to_student()
    print(p.find_min_calls())

if __name__ == '__main__':
    main()
