class Node:
    def __init__(self, v, n):
        self.v = v
        self.next = n


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def quick_sort_recur(self, head, tail):
        # base case
        if head is None or head == tail:
            return head
        new_head = new_tail = None
        pivot, new_head, new_tail = self._partition(head, tail, new_head, new_tail)
        if new_head != pivot:
            tmp = new_head
            while tmp.next != pivot:
                tmp = tmp.next
            tmp.next = None
            new_head = self.quick_sort_recur(new_head, tmp)
            tmp = self._get_tail(new_head)
            tmp.next = pivot
        pivot.next = self.quick_sort_recur(pivot.next, new_tail)
        return new_head

    def push(self, v):
        n = Node(v, self.head)
        self.head = n

    def _partition(self, head, tail, new_head, new_tail):
        pivot = tail
        prev, cur, end = None, head, pivot
        while cur != pivot:
            if cur.v < pivot.v:
                if new_head is None:
                    new_head = cur
                prev = cur
                cur = cur.next
            else:
                if prev is not None:
                    prev.next = cur.next
                temp = cur.next
                cur.next = None
                end.next = cur
                end = cur
                cur = temp
        if new_head is None:
            new_head = pivot
        new_tail = end
        return pivot, new_head, new_tail

    def _get_tail(self, node):
        tail = node
        while tail.next is not None:
            tail = tail.next
        return tail

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.v, end=' ')
            tmp = tmp.next
        print()


l = SinglyLinkedList()

l.push(3)
l.push(2)
l.push(3)
l.push(1)
l.push(2)
l.push(5)
l.push(3)
l.push(4)
l.print_list()
l.head = l.quick_sort_recur(l.head, l._get_tail(l.head))
l.print_list()
