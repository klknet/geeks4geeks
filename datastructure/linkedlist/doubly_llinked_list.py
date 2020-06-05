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
    def __init__(self, s=None, sign=0):
        self.head = self.tail = None
        self.length = 0
        self.sign = sign
        if s is not None:
            self.insert(s)

    def insert(self, s):
        for i in range(len(s)):
            self.insertEnd(s[i])

    def insertFront(self, data):
        self.length += 1
        node = _DoubleNode(data=int(data), n=self.head)
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node
        self.head = node

    def insertEnd(self, data):
        self.length += 1
        node = _DoubleNode(data=int(data), prev=self.tail)
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node
        self.tail = node

    def trim(self):
        cur = self.head
        while cur:
            if cur.data != 0:
                break
            self.head = cur.next
            if cur.next:
                cur.next.prev = None
            cur = cur.next
            self.length -= 1
        return self

    def abs(self):
        self.sign = 0
        return self

    def empty(self):
        return self.length == 0 or self.head.data == 0

    def neg(self):
        self.sign = 1
        return self

    def display(self):
        if not self.head:
            print(0)
            return
        if self.sign == 1:
            print('-', end='')
        cur = self.head
        while cur:
            print(cur.data, end='')
            cur = cur.next
        print()

    def __str__(self):
        return str(self.data)

    @staticmethod
    def add(a: 'HugeInt', b: 'HugeInt') -> 'HugeInt':
        if a.empty():
            return b
        if b.empty():
            return a
        if a.sign == 0 and b.sign == 1:
            res = HugeInt.diff(a, b.abs())
            b.neg()
            return res
        if a.sign == 1 and b.sign == 0:
            res = HugeInt.diff(b, a.abs())
            a.neg()
            return res
        if a.sign == 1 and b.sign == 1:
            res = HugeInt.add(a.abs(), b.abs()).neg()
            b.neg()
            a.neg()
            return res
        res = HugeInt()
        c = 0
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
            res.insertFront(s)
        if c:
            res.insertFront(c)
        return res

    @staticmethod
    def diff(a: 'HugeInt', b: 'HugeInt') -> 'HugeInt':
        r = HugeInt.cmp(a, b)
        if r == 0:
            return HugeInt()
        if a.sign == 0 and b.sign == 1:
            res = HugeInt.add(a, b.abs())
            b.neg()
            return res
        if a.sign == 1 and b.sign == 0:
            res = HugeInt.add(a.abs(), b).neg()
            a.neg()
            return res
        if r == -1 and a.sign == b.sign == 0:
            a, b = b, a
        c = 0
        atail = a.tail
        btail = b.tail
        res = HugeInt(sign=1 if r == -1 else 0)
        while atail and btail:
            d = (atail.data - btail.data - c + 10) % 10
            c = 1 if atail.data - btail.data - c < 0 else 0
            res.insertFront(d)
            atail = atail.prev
            btail = btail.prev
        while atail:
            res.insertFront(atail.data - c)
            atail = atail.prev
        return res.trim()

    @staticmethod
    def cmp(a: 'HugeInt', b: 'HugeInt'):
        if a.sign == b.sign:
            res = 0
            if a.length > b.length:
                res = 1
            elif a.length < b.length:
                res = -1
            else:
                ahead, bhead = a.head, b.head
                while ahead:
                    if ahead.data == bhead.data:
                        ahead = ahead.next
                        bhead = bhead.next
                    elif ahead.data > bhead.data:
                        res = 1
                        break
                    else:
                        res = -1
                        break
            return res if a.sign == 0 else -res
        elif a.sign == 0 and b.sign == 1:
            return 1
        else:
            return -1

    @staticmethod
    def multiply(a: 'HugeInt', b: 'HugeInt') -> 'HugeInt':
        if a.empty() or b.empty():
            return HugeInt()
        btail = b.tail
        s = []
        k = 0
        res = HugeInt()
        while btail is not None:
            atail = a.tail
            h = HugeInt()
            s.append(h)
            m = c = 0
            while atail is not None:
                m = (atail.data * btail.data + c) % 10
                c = (atail.data * btail.data + c) // 10
                h.insertFront(m)
                atail = atail.prev
            if c:
                h.insertFront(c)
            # 错位相乘时补0
            for i in range(k):
                h.insertEnd(0)
            res = HugeInt.add(res, h)
            btail = btail.prev
            k += 1
        if a.sign + b.sign == 1:
            res.sign = 1
        return res

    @staticmethod
    def quotient(a: 'HugeInt', b: 'HugeInt') -> 'HugeInt':
        sign = 1 if a.sign + b.sign == 1 else 0
        r = HugeInt.cmp(a.abs(), b.abs())
        if r == -1:
            return HugeInt('0')
        if r == 0:
            return HugeInt('1')
        ex = HugeInt()
        ahead = a.head
        for i in range(b.length):
            ex.insertEnd(ahead.data)
            ahead = ahead.next
        res = HugeInt(sign=sign)
        while True:
            for i in range(1, 11):
                pr = HugeInt.multiply(b, HugeInt(str(i)))
                if HugeInt.cmp(ex, pr) == -1:
                    break
            res.insertEnd(i - 1)
            if i > 1:
                ex = HugeInt.diff(ex, HugeInt.multiply(b, HugeInt(str(i - 1))))
            if not ahead:
                break
            ex.insertEnd(ahead.data)
            ahead = ahead.next
        return res.trim()


def rotate_dll(head, n):
    """
    Rotate a doubly linked list by N nodes.
    :param head:
    :param n:
    :return:
    """
    if n <= 0:
        return head
    cur = head
    for i in range(n):
        cur = cur.next
    cur.prev.next = None
    cur.prev = None
    t = cur.tail()
    t.next = head
    head.prev = t
    return cur


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.rear = None

    def push(self, data, priority):
        pn = PriorityQueue.PriorityNode(data, priority)
        if self.head is None:
            self.head = self.rear = pn
        else:
            if self.head.priority > priority:
                pn.next = self.head
                self.head.prev = pn
                self.head = pn
            elif self.rear.priority < priority:
                pn.prev = self.rear
                self.rear.next = pn
                self.rear = pn
            else:
                cur = self.head
                while cur:
                    if cur.priority > priority:
                        break
                    cur = cur.next
                prev = cur.prev
                prev.next = pn
                cur.prev = pn
                pn.prev = prev
                pn.next = cur

    def peek(self):
        if self.head:
            return self.head.data

    def pop(self):
        if self.head:
            cur = self.head
            n = cur.next
            cur.next = None
            if n:
                n.prev = None
            else:
                self.rear = None
            self.head = n
            return cur.data

    class PriorityNode(_DoubleNode):
        def __init__(self, data=None, priority=0, prev=None, n=None):
            _DoubleNode.__init__(self, prev, data, n)
            self.priority = priority


def reverse_in_groups(node, n):
    """
    Reverse a doubly linked list in groups of given size.
    :param node:
    :param n:
    :return:
    """
    cur = node
    prev = None
    i = n
    while cur and i > 0:
        tmp = cur.next
        cur.next = prev
        cur.prev = tmp
        prev = cur
        cur = tmp
        i -= 1
    prev.prev = None
    if cur:
        newhead = reverse_in_groups(cur, n)
        node.next = newhead
        newhead.prev = node
    return prev


class CircularDoublyLinkedList(object):
    def __init__(self, head: _DoubleNode = None):
        self.head = head

    def insertFront(self, data):
        if not self.head:
            self.head = _DoubleNode(data=data)
            self.head.prev = self.head
            self.head.next = self.head
            return
        node = _DoubleNode(self.head.prev, data=data, n=self.head)
        self.head.prev.next = node
        self.head.prev = node
        self.head = node

    def insertRear(self, data):
        if not self.head:
            self.head = _DoubleNode(data=data)
            self.head.prev = self.head
            self.head.next = self.head
            return
        node = _DoubleNode(self.head.prev, data=data, n=self.head)
        self.head.prev.next = node
        self.head.prev = node

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
            if cur == self.head:
                break
        print()

    def delete(self, value):
        cur = self.valueOf(value)
        if not cur:
            return
        if cur.next == cur:
            self.head=None
            return
        if cur == self.head:
            self.head = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.next
        cur.next = None
        cur.prev = None

    def insertAfter(self, v1, v2):
        cur = self.valueOf(v1)
        if not cur:
            return
        node = _DoubleNode(cur, data=v2, n=cur.next)
        n = cur.next
        n.prev = node
        cur.next = node

    def valueOf(self, value):
        cur = self.head
        found = False
        while cur:
            if cur.data == value:
                found = True
                break
            cur = cur.next
            if cur == self.head:
                break
        return cur if found else None


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
    b = HugeInt('456789123456789123456789123456789123456789123456789', sign=1)
    a = HugeInt('1111', sign=0)
    b = HugeInt('9999', sign=0)
    HugeInt.add(a, b).display()
    HugeInt.multiply(a, b).display()
    HugeInt.diff(a, b).display()
    HugeInt.quotient(a, b).display()
    d = DoublyLinkedList()
    d.add_all([1, 2, 3, 4, 5])
    d.head = rotate_dll(d.head, 2)
    d.traverse()
    p = PriorityQueue()
    p.push(2, 3)
    p.push(3, 4)
    p.push(4, 5)
    p.push(5, 6)
    p.push(6, 7)
    p.push(1, 12)
    print(p.peek())
    print(p.pop())
    print(p.pop())
    d = DoublyLinkedList()
    d.add_all([1, 2, 3, 4, 5, 6, 7, 8])
    d.head = reverse_in_groups(d.head, 3)
    d.traverse()
    d.reverseTraverse()
    c = CircularDoublyLinkedList()
    c.insertFront(1)
    c.insertFront(3)
    c.insertFront(5)
    c.insertRear(4)
    c.insertRear(6)
    c.insertRear(8)
    c.insertAfter(5, 5.5)
    c.insertAfter(1, 1.5)
    c.insertAfter(8, 8.5)
    c.delete(5)
    c.delete(8.5)
    c.delete(1.5)
    c.traverse()
