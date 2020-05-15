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


class CircularQueue:
    def __init__(self):
        self.__rear = None

    def enqueue(self, data):
        if not self.__rear:
            self.__rear = _Node(data)
            self.__rear.next = self.__rear
            return
        n = _Node(data, self.__rear.next)
        self.__rear.next = n
        self.__rear = n

    def dequeue(self):
        if not self.__rear:
            return None
        f = self.__rear.next
        if self.__rear == f:
            self.__rear = None
        else:
            self.__rear.next = f.next

    def front(self):
        if not self.__rear:
            return None
        return self.__rear.next.data

    def rear(self):
        if not self.__rear:
            return None
        return self.__rear.data

    def traverse(self):
        traverse(self.__rear)


class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def traverse(self):
        cur = self
        while True:
            print(cur.data, end=' ')
            cur = cur.right
            if cur == self:
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
    if data <= cur.data:
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


def convert_double_list(root):
    """
    Convert a Binary Tree to a Circular Doubly Linked List.
    :param root:
    :return:
    """
    if not root:
        return
    leftTree = convert_double_list(root.left)
    rightTree = convert_double_list(root.right)
    root.left = root.right = root
    return concatenate(concatenate(leftTree, root), rightTree)


def concatenate(leftTree, rightTree):
    if not leftTree:
        return rightTree
    if not rightTree:
        return leftTree
    leftTail = leftTree.left
    rightTail = rightTree.left

    leftTail.right = rightTree
    rightTree.left = leftTail
    leftTree.left = rightTail
    rightTail.right = leftTree
    return leftTree


def insert_head(node, data):
    if not node:
        node = _Node(data)
        node.next = node
        return
    head = node.next
    n = _Node(data, head)
    node.next = n


def insert_end(node, data):
    if not node:
        node = _Node(data)
        node.next = node
        return
    head = node.next
    n = _Node(data, head)
    node.next = n
    return n


def traverse(node):
    if not node:
        return
    head = node.next
    cur = head
    while True:
        print(cur.data, end=' ')
        cur = cur.next
        if cur == head:
            break
    print()


def insert_after(node, data, item):
    cur = node
    exist = False
    while True:
        if cur.data == data:
            exist = True
            break
        cur = cur.next
        if cur == node:
            break
    if exist:
        cur.next = _Node(item, cur.next)
        if cur == node:
            return cur.next
    return node


def delete(node, data):
    if not node:
        return None
    head = node.next
    cur = head
    prev = node
    exist = False
    while True:
        if cur.data == data:
            exist = True
            break
        prev = cur
        cur = cur.next
        if cur == head:
            break
    if exist:
        if cur == node:
            node = prev
        prev.next = cur.next
        cur.next = None
    return node


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
    root = BinaryNode(10, BinaryNode(12, BinaryNode(25), BinaryNode(30)), BinaryNode(15, BinaryNode(36)))
    head = convert_double_list(root)
    head.traverse()
    n = _Node(0)
    n.next = n
    insert_head(n, -1)
    insert_head(n, -2)
    insert_head(n, -3)
    traverse(n)
    n = insert_end(n, 1)
    n = insert_end(n, 2)
    n = insert_end(n, 3)
    traverse(n)
    n = insert_after(n, 2, 2.5)
    n = insert_after(n, 3, 3.5)
    n = insert_after(n, -2, -1.5)
    traverse(n)
    n = delete(n, -1.5)
    n = delete(n, 2.5)
    n = delete(n, 3.5)
    n = delete(n, -3)
    n = delete(n, -13)
    traverse(n)

    cq = CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.traverse()

    print(cq.front())
    print(cq.rear())

    cq.dequeue()
    cq.dequeue()
    # cq.dequeue()
    cq.traverse()