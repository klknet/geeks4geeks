"""
Linked list.
"""


class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinedList(object):
    def __init__(self):
        self.head = None
        self.num = 0

    def add_node(self, data):
        node = _Node(data)
        node.next = self.head
        self.head = node
        self.num += 1

    def add_all(self, arr):
        for i in range(len(arr) - 1, -1, -1):
            self.add_node(arr[i])

    def remove_all(self):
        curr = self.head
        self.head = None
        while curr is not None:
            n = curr.next
            curr = None
            curr = n
        self.num = 0

    def push(self, data):
        node = _Node(data)
        node.next = self.head
        self.head = node
        self.num += 1

    def pop(self, idx=None):
        if self.num == 0:
            raise Exception("empty list")
        if idx is None:
            idx = self.num - 1
        if idx >= self.num:
            raise Exception("Index Out Of Boundary Exception")
        cur = self.head
        prev = None
        for i in range(idx):
            prev = cur
            cur = cur.next
        res = cur.data
        self.num -= 1
        if prev is None:
            self.head = cur.next
        elif cur.next is None:
            prev.next = None
        else:
            prev.next = cur.next
            cur.next = None
        return res

    def exist(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                return True
            cur = cur.next
        return False

    def get_from_end(self, idx):
        if idx >= self.num:
            raise Exception("Out of Index Boundary Exception")
        idx = self.num-idx
        return self.get(idx)

    def get(self, idx):
        cur = self.head
        for i in range(idx):
            if cur:
                cur = cur.next
            else:
                break
        if cur:
            return cur.data
        return None

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def size(self):
        return self.num


if __name__ == '__main__':
    l = LinedList()
    l.add_all([0, 1, 2, 3, 4, 5, 6])
    print(l.exist(1))
    print(l.exist(10))
    print(l.get(2))
    print(l.get_from_end(2))
    l.push(7)
    l.traverse()
    print(l.pop(2))
    print(l.pop())
    l.traverse()
    # l.remove_all()
