import heapq

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

    def traverse(self, split=None):
        self.head.traverse(split)

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


class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


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


def push(node):
    global args
    if not args['tail']:
        args['tail'] = node
        node.left = node.mid = node.right = None
        return args['tail']
    args['tail'].right = node
    node.left = args['tail']
    node.mid = node.right = None
    args['tail'] = node


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


def remove(node):
    r = node.next
    n = r.next
    r.prev = None
    r.next = None
    node.next = n
    if n:
        n.prev = node


def remove_duplicate(node):
    cur = node
    while cur:
        if cur.next and cur.next.data == cur.data:
            remove(cur)
            continue
        cur = cur.next


def remove_all_occur(dll, data):
    node = dll.head
    prev = None
    cur = node
    while cur:
        if cur.data == data:
            n = cur.next
            cur.next = None
            cur.prev = None
            if prev:
                prev.next = n
                cur = n
            else:
                node = n
                cur = n
            if n:
                n.prev = prev
        else:
            prev = cur
            cur = cur.next
    dll.head = node


def sort_biotonic_dll(head):
    cur = head
    while cur:
        if cur.next and cur.next.data < cur.data:
            break
        cur = cur.next
    if not cur:
        return head
    second = cur.next
    cur.next = None
    second.prev = None
    second = reverse(second)
    return merge(head, second)


def sort_k_sorted(head, k):
    """
    Sort a k-sorted node.
    :param head:
    :param k:
    :return:
    """
    newhead = None
    priorityQueue = []
    cur = head
    for i in range(k + 1):
        if cur:
            heapq.heappush(priorityQueue, cur)
            cur = cur.next
    last = None
    while len(priorityQueue) > 0:
        node = heapq.heappop(priorityQueue)
        if not newhead:
            newhead = node
            node.prev = None
            last = node
        else:
            last.next = node
            node.prev = last
            last = node
        if cur:
            heapq.heappush(priorityQueue, cur)
            cur = cur.next
    last.next = None
    return newhead


def convert2Dll(tree):
    """
    Convert a binary tree into doubly linked list in inorder.
    :param tree:
    :return:
    """
    if not tree:
        return
    left = tree.left
    right = tree.right
    tree.left = None
    tree.right = None
    return link(link(convert2Dll(left), tree), convert2Dll(right))


def link(left, right):
    if not left:
        return right
    if not right:
        return left
    tail = binaryTreeTail(left)
    tail.right = right
    right.left = tail
    return left


args = {'head': None, 'tail': None}


def tree2dll(root):
    global args
    if not root:
        return
    tree2dll(root.right)
    root.right = args['head']
    if args['head']:
        args['head'].left = root
    args['head'] = root
    tree2dll(root.left)


def btTraversel():
    global args
    traverse(args['head'])
    reverseTraverse(args['head'])


def binaryTreeTail(root):
    tail = root
    while True:
        if tail and not tail.right:
            break
        tail = tail.right
    return tail


def traverse(bt):
    cur = bt
    while cur:
        print(cur.data, end=' ')
        cur = cur.right
    print()


def reverseTraverse(bt):
    tail = binaryTreeTail(bt)
    while tail:
        print(tail.data, end=' ')
        tail = tail.left
    print()


class HugeInt(object):
    def __init__(self, s=None):
        self.head = self.tail = None
        if s is not None:
            self.insert(s)

    def insert(self, s):
        for i in range(len(s)):
            self.insertEnd(s[i])

    def insertFront(self, data):
        node = _DoubleNode(data=int(data), n=self.head)
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node
        self.head = node

    def insertEnd(self, data):
        node = _DoubleNode(data=int(data), prev=self.tail)
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node
        self.tail = node

    def __str__(self):
        return str(self.data)

    @staticmethod
    def add(a: 'HugeInt', b: 'HugeInt') -> DoublyLinkedList:
        res = DoublyLinkedList()
        s = c = 0
        atail = a.tail
        btail = b.tail
        while atail is not None or btail is not None:
            if atail is None and btail is not None:
                s = (btail.data + c) % 10
                c = (btail.data + c) // 10
                btail = btail.prev
            elif atail is not None and btail is None:
                s = (atail.data + c) % 10
                c = (atail.data + c) // 10
                atail = atail.prev
            else:
                s = (atail.data + btail.data + c) % 10
                c = (atail.data + btail.data + c) // 10
                atail = atail.prev
                btail = btail.prev
            res.push(s)
        if c:
            res.push(c)
        return res


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
    d = DoublyLinkedList()
    d.add_all([4, 4, 4, 4, 6, 8, 8, 10, 12, 12])
    remove_duplicate(d.head)
    d.traverse()
    d = DoublyLinkedList()
    d.add_all([2, 2, 10, 8, 4, 2, 5, 2])
    remove_all_occur(d, 2)
    d.traverse()
    d = DoublyLinkedList()
    # d.add_all([2, 5, 7, 12, 10, 6, 4, 1])
    # d.add_all([5, 4, 3, 2, 1])
    d.add_all([1, 2, 3, 4, 5])
    d.head = sort_biotonic_dll(d.head)
    d.traverse()
    d = DoublyLinkedList()
    d.add_all([3, 6, 2, 12, 56, 8])
    d.head = sort_k_sorted(d.head, 2)
    d.traverse()
    d.reverseTraverse()
    bt = BinaryNode(10, BinaryNode(12, BinaryNode(25), BinaryNode(30)), BinaryNode(15, BinaryNode(36)))
    newhead = convert2Dll(bt)
    traverse(newhead)
    reverseTraverse(newhead)
    bt = BinaryNode(10, BinaryNode(12, BinaryNode(25), BinaryNode(30)), BinaryNode(15, BinaryNode(36)))
    tree2dll(bt)
    btTraversel()
    a = HugeInt('123456789123456789123456789123456789123456789123456789')
    b = HugeInt('456789123456789123456789123456789123456789123456789')
    HugeInt.add(a, b).traverse('')
