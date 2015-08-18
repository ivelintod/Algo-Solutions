class LinkedList:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def make_links(self, elem, node):
        elem.next = node

    def sequential_links(self, n, seq):
        for node in seq:
            self.make_links(n, LinkedList(node))
            self.sequential_links(LinkedList(node), seq)

    def print_nodes(self, n):
        if n == None:
            return
        print n,
        self.print_nodes(n.next)


class KLists:

    def __init__(self):
        pass





def main():
    n1 = LinkedList(3)
    n2 = LinkedList(5)
    n3 = LinkedList(7)
    n4 = LinkedList(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n1.print_nodes(n1)




if __name__ =='__main__':
    main()
