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
        while True:
            print(tmp.data, end=' ')
            tmp = tmp.next
            if tmp == self.head:
                break
        print()


def half(ll):
    """
    Split a circular linked list into two halves.
    :param ll:
    :return:
    """
    if not ll.head:
        return
    if ll.head.next == ll.head:
        ll.traverse()
        return
    cur = ll.head
    fast, slow = cur.next, cur
    while fast and fast.next != cur:
        fast = fast.next
        if fast and fast.next != cur:
            fast = fast.next
            slow = slow.next
    tmp = slow.next
    slow.next = cur
    fast.next = tmp
    left = CircularLinkedList(cur)
    right = CircularLinkedList(tmp)
    left.traverse()
    right.traverse()


def insert(ll, data):
    cur = ll.head
    if data<=cur.data:
        t = ll.tail()
        t.next = _Node(data, ll.head)
        ll.head = t.next
        ll.traverse()
        return
    while True:
        if cur.data < data <= cur.next.data:
            break
        if cur.next == ll.head:
            break
        cur = cur.next
    tmp = cur.next
    cur.next = _Node(data, tmp)
    ll.traverse()



if __name__ == '__main__':
    c = CircularLinkedList()
    c.push(0)
    # c.add_all([1, 2, 3, 4, 5, 6])
    # c.push(7)
    c.traverse()
    half(c)
    c = CircularLinkedList()
    c.add_all([1, 3, 5, 7, 9])
    insert(c, 10)
