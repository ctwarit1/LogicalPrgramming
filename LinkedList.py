class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display_LL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end=" ")
                n = n.ref

    def add_elem(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_elem_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def rev_LL(self, data):
        curr = self.head



obj = LinkedList()

obj.add_elem_end(5)

obj.add_elem(1)
obj.add_elem(2)
obj.add_elem(3)

obj.display_LL()
