def min_max_heap(tree):
        s = 0
        lvl = 1
        if tree[s * 2 + 1] < tree[s] or tree[s * 2 + 2] < tree[s]:
                return "NO"
        #s = 2
        lvl += 1
        temp_num_items = 0
        new_lvl_num_items = 2
        try:
                while True:
                        for item in range(new_lvl_num_items):
                                s += 1
                                if lvl % 2 == 0:
                                        if tree[s] < tree[s * 2 + 1] or tree[s] < tree[s * 2 + 2] or tree[(s - 1) // 2] > tree[s * 2 + 1] or tree[(s - 1) // 2] > tree[s * 2 + 2]:
                                                return "NO"
                                        temp_num_items += 2
                                else:
                                        if tree[s] > tree[s * 2 + 1] or tree[s] > tree[s * 2 + 2] or tree[(s - 1) // 2] < tree[s * 2 + 1] or tree[(s - 1) // 2] < tree[s * 2 + 2]:
                                                return "NO"
                                        temp_num_items += 2

                        new_lvl_num_items = temp_num_items
                        temp_num_items = 0
                        lvl += 1
        except IndexError:
                return "YES"

def main():
        num = int(input())
        tree_inp = input()
        tree = [int(x) for x in tree_inp.split()]
        print(min_max_heap(tree))

if __name__ == '__main__':
        main()
