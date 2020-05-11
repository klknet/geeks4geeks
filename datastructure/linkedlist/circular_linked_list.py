from datastructure.linkedlist.base_linked_list import _Node


class CircularLinkedList:
    def __init__(self, node=None):
        self.head = node

    def push(self, data):
        node = _Node(data, self.head)
        if self.head:
            t = self.tail()
            t.next = node
        else:
            node.next = node
        self.head = node

    def tail(self):
        if not self.head:
            return None
        tmp = self.head
        while tmp.next != self.head:
            tmp = tmp.next
        return tmp

    def add_all(self, arr):
        t = self.tail()
        if t:
            for i in arr:
                t.next = _Node(i)
                t = t.next
            t.next = self.head
        else:
            tmp = self.head
            for i in arr:
                if not tmp:
                    tmp = _Node(i)
                    self.head = tmp
                else:
                    tmp.next = _Node(i)
                    tmp = tmp.next
            tmp.next = self.head

    def traverse(self):
        tmp = self.head
        while tmp.next != self.head:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()


if __name__ == '__main__':
    c = CircularLinkedList()
    c.push(0)
    c.add_all([1, 2, 3, 4, 5, 6])
    c.push(7)
    c.traverse()
