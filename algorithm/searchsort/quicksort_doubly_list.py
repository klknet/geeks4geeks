class Node:
    def __init__(self, v=None, prev=None, next=None):
        self.v = v
        self.prev = prev
        self.next = next

    @staticmethod
    def tail(node):
        while node.next is not None:
            node = node.next
        return node


class LinkedList:
    def __init__(self):
        self.head = None

    def quick_sort(self):
        if self.head is None:
            print('no value')
            exit()
        self._quick_recur(self.head, Node.tail(self.head))

    def _quick_recur(self, head, end):
        pivot = self._partition(head, end)
        if pivot != head:
            self._quick_recur(head, pivot.prev)
        if pivot != end:
            self._quick_recur(pivot.next, end)

    def _partition(self, head, end):
        pivot = end
        i, j = head.prev, head
        while j != pivot:
            if j.v <= pivot.v:
                i = head if i is None else i.next
                i.v, j.v = j.v, i.v
            j = j.next
        i = head if i is None else i.next
        i.v, pivot.v = pivot.v, i.v
        return i

    def push(self, v):
        n = Node(v, None, self.head)
        if self.head is None:
            self.head = n
            return
        self.head.prev = n
        self.head = n

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.v, end=' ')
            tmp = tmp.next
        print()


if __name__ == '__main__':
    l = LinkedList()
    l.push(3)
    l.push(2)
    l.push(3)
    l.push(1)
    l.push(2)
    l.push(24)
    l.push(5)
    l.push(3)
    l.push(4)
    l.push(-8)
    l.print()
    l.quick_sort()
    l.print()
