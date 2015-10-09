class Heap:

    def __init__(self):
        self.heap_array = list()
        self.merged_list = list()

    def insert(self, cand):
        arr = self.heap_array
        if len(arr) == 1:
            arr.append(cand)
            return
        arr.append(cand)
        index = len(arr) - 1
        while index:
            if arr[index][0] < arr[(index - 1) // 2][0]:
                arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
            index = (index - 1) // 2

    @property
    def first(self):
        return self.heap_array[0]

    def pop_and_replace(self, cand):
        res = self.heap_array.pop(0)
        self.merged_list.append(res)
        self.heap_array.insert(0, cand)
        self.heapify_partly(self.heap_array)

    def heapify_partly(self, arr):
        index = 0
        try:
            while True:
                if arr[index * 2 + 1][0] < arr[index * 2 + 2][0]:
                    if arr[index][0] > arr[index * 2 + 1][0]:
                        arr[index], arr[index * 2 + 1] = arr[index * 2 + 1], arr[index]
                        index = index * 2 + 1
                    else:
                        break
                else:
                    if arr[index][0] > arr[index * 2 + 2][0]:
                        arr[index], arr[index * 2 + 2] = arr[index * 2 + 2], arr[index]
                        index = index * 2 + 2
                    else:
                        break
        except IndexError:
            pass

        try:
            if arr[index][0] > arr[index * 2 + 1][0]:
                arr[index], arr[index * 2 + 1] = arr[index * 2 + 1], arr[index]
        except IndexError:
            pass

        try:
            if arr[index][0] > arr[index * 2 + 2][0]:
                arr[index], arr[index * 2 + 2] = arr[index * 2 + 2], arr[index]
        except IndexError:
            pass


class K_lists:

    def __init__(self, list_of_arrays):
        self.heap = Heap()
        self.arr = list_of_arrays

    def merge_lists(self):
        for i in range(len(self.arr)):
            if len(self.arr[i]):
                self.heap.insert((self.arr[i][0], i))
        count_empty_arrs = 0
        while True:
            first = self.heap.first
            if len(self.arr[first[1]]) > 1:
                self.arr[first[1]].pop(0)
                self.heap.pop_and_replace((self.arr[first[1]][0], first[1]))
            else:
                self.heap.merged_list.append((first[0], None))
                self.heap.heap_array.pop(0)
                self.heap.heap_array.insert(0, (10000000, None))
                self.heap.heapify_partly(self.heap.heap_array)
                count_empty_arrs += 1
            if count_empty_arrs == len(self.arr):
                break
        return self.heap.merged_list

def main():
    num = int(input())
    a = []
    for i in range(num):
        j = input()
        a.append([int(x) for x in j.split()[:len(j.split()) - 1]])
    k = K_lists(a)
    res = [x[0] for x in k.merge_lists()]
    for r in res:
        print(r, end=' ')

if __name__ == '__main__':
    main()

