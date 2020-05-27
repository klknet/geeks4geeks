from datastructure.linkedlist.base_linked_list import _DoubleNode, LinkedList


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        if not self.head:
            self.head = _DoubleNode(None, data, None)
            return
        node = _DoubleNode(None, data, self.head)
        self.head.prev = node
        self.head = node
        return self

    def add_all(self, arr):
        for i in arr:
            self.append(i)

    def append(self, data):
        t = self.tail()
        if not t:
            self.head = _DoubleNode(None, data, None)
            return
        node = _DoubleNode(t, data, None)
        t.next = node

    def insertAfter(self, prevNode, data):
        if not prevNode:
            return
        node = _DoubleNode(prevNode, data, prevNode.next)
        if prevNode.next:
            prevNode.next.prev = node
        prevNode.next = node

    def delete(self, data):
        node = self.valueOf(data)
        if not node:
            return
        if self.head == node:
            self.head = node.next
            node.next = None
            if self.head:
                node.next.prev = None
        else:
            prev = node.prev
            n = node.next
            if prev:
                prev.next = n
            if n:
                n.prev = prev
            node.prev = None
            node.next = None

    def valueOf(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                break
            cur = cur.next
        return cur

    def traverse(self):
        self.head.traverse()

    def reverseTraverse(self):
        self.head.reverseTraverse()

    def tail(self):
        cur = self.head
        while cur:
            if not cur.next:
                break
            cur = cur.next
        return cur


class TernaryNode:
    def __init__(self, data=None, left=None, mid=None, right=None):
        self.data = data
        self.left = left
        self.mid = mid
        self.right = right


def reverse(node):
    if not node:
        return
    newhead = reverse(node.next)
    node.prev, node.next = node.next, node.prev
    return newhead if newhead else node


def quicksort(head):
    last = head.tail()
    _quicksort(head, last)


def _quicksort(head, last):
    if head is not None and last is not None and head != last and head != last.next:
        pivot = partition(head, last)
        _quicksort(head, pivot.prev)
        _quicksort(pivot.next, last)


def partition(head, last):
    i = j = head
    pivot = last
    while i != last:
        if i.data <= pivot.data:
            i.data, j.data = j.data, i.data
            j = j.next
        i = i.next
    i.data, j.data = j.data, i.data
    return j


def swapKth(head, k):
    """
    Swap Kth node from beginning with Kth node from end in a linkedlist.
    :param head:
    :param k:
    :return:
    """
    if not head:
        return
    n = head.count()
    if k > n:
        return
    if (2 * k - 1) == n:
        return
    x = head
    x_prev = None
    for i in range(1, k):
        x_prev = x
        x = x.next
    y = head
    y_prev = None
    for i in range(1, n - k + 1):
        y_prev = y
        y = y.next
    if x_prev:
        x_prev.next = y
    if y_prev:
        y_prev.next = x
    x.next, y.next = y.next, x.next
    if k == 1:
        return y
    if k == n:
        return x
    return head


def merge_sort(head):
    if not head:
        return
    if not head.next:
        return head
    mid = middle(head)
    n = mid.next
    mid.next = None
    if n:
        n.prev = None
    left = merge_sort(head)
    right = merge_sort(n)
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    newhead = None
    if left.data > right.data:
        newhead = right
        node = merge(left, right.next)
        newhead.next = node
        node.prev = newhead
    else:
        newhead = left
        node = merge(left.next, right)
        newhead.next = node
        node.prev = newhead
    return newhead


def middle(node):
    slow, fast = node, node.next
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
    return slow


def build_dll_from_ternary_tree(root):
    """
    Create a Doubly Linked List from a ternary tree.
    :param root:
    :return:
    """
    if not root:
        return
    left = root.left
    mid = root.mid
    right = root.right
    push(root)
    build_dll_from_ternary_tree(left)
    build_dll_from_ternary_tree(mid)
    build_dll_from_ternary_tree(right)


tail = None


def push(node):
    global tail
    if not tail:
        tail = node
        node.left = node.mid = node.right = None
        return tail
    tail.right = node
    node.left = tail
    node.mid = node.right = None
    tail = node


def traverseTernaryNode(root):
    cur = root
    while cur:
        print(cur.data, end=' ')
        cur = cur.right
    print()


def pairs_with_given_sum(head, x):
    """
    Find pairs with given sum in doubly linked list.
    :param head:
    :param x:
    :return:
    """
    tail = head.tail()
    while head != tail:
        if head.data + tail.data > x:
            tail = tail.prev
        elif head.data + tail.data < x:
            head = head.next
        else:
            print("(%d, %d)" % (head.data, tail.data))
            head = head.next


def insert_in_sorted_list(node, data):
    prev = None
    cur = node
    while cur:
        if cur.data > data:
            break
        prev = cur
        cur = cur.next
    n = _DoubleNode(prev, data, cur)
    if prev:
        prev.next = n
    else:
        node = n
    if cur:
        cur.prev = n
    return node


def triplet_dll(node, x):
    """
    Count triplets in a sorted doubly linked list whose sum is equal to a given value x.
    :param node:
    :param x:
    :return:
    """
    first = node
    t = node.tail()
    while first:
        r = x - first.data
        second = first.next
        third = t
        while second and second != third:
            if second.data + third.data == r:
                print("(%d, %d, %d)" % (first.data, second.data, third.data))
                second = second.next
            elif second.data + third.data > r:
                third = third.prev
            else:
                second = second.next
        first = first.next


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.push(1)
    d.push(2)
    d.append(3)
    d.append(6)
    d.insertAfter(d.valueOf(3), 5)
    d.insertAfter(d.valueOf(6), 7)
    d.insertAfter(d.valueOf(1), 8)
    d.insertAfter(d.valueOf(10), 9)
    d.traverse()
    d.delete(7)
    d.delete(1)
    d.delete(8)
    d.traverse()
    print('===========')
    d.head = reverse(d.head)
    d.traverse()
    d.reverseTraverse
    d = DoublyLinkedList()
    d.add_all([5, 15, 7, 5, 1, 10])
    quicksort(d.head)
    d.traverse()
    print('--------------')
    d = LinkedList()
    d.add_all([1, 2, 3, 4, 5, 6])
    d.head = swapKth(d.head, 1)
    d.traverse()
    d.head = swapKth(d.head, 2)
    d.traverse()
    d.head = swapKth(d.head, 6)
    d.traverse()
    d = DoublyLinkedList()
    d.add_all([5, 20, 4, 3, 30, 10])
    d.head = merge_sort(d.head)
    d.traverse()
    d.reverseTraverse()
    t = TernaryNode(30, TernaryNode(5, TernaryNode(1), TernaryNode(4), TernaryNode(8)),
                    TernaryNode(11, TernaryNode(6), TernaryNode(7), TernaryNode(15)),
                    TernaryNode(63, TernaryNode(31), TernaryNode(55), TernaryNode(65)))
    build_dll_from_ternary_tree(t)
    traverseTernaryNode(t)
    d = DoublyLinkedList()
    d.add_all([1, 2, 4, 5, 6, 8, 9])
    pairs_with_given_sum(d.head, 7)
    d.head = insert_in_sorted_list(d.head, 3)
    d.head = insert_in_sorted_list(d.head, -1)
    d.head = insert_in_sorted_list(d.head, 10)
    d.traverse()
    d = DoublyLinkedList()
    d.add_all(range(1, 10))
    triplet_dll(d.head, 17)
