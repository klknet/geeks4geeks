"""
Linked list.
"""


class _Node:
    def __init__(self, data, n=None):
        self.data = data
        self.next = n

    def traverse(self):
        cur = self
        while True:
            print(cur.data, end='  ')
            if not cur.next:
                break
            cur = cur.next
        print()

    def add_all(self, arr):
        cur = self
        for d in arr:
            cur.next = _Node(d)
            cur = cur.next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.num = 0

    def append(self, data):
        """
        Append a element at end of list.
        :param data:
        :return:
        """
        if self.empty():
            self.head = _Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = _Node(data)
        self.num += 1

    def add_all(self, arr):
        """
        Add array elements to list.
        :param arr:
        :return:
        """
        for i in range(len(arr) - 1, -1, -1):
            self.push(arr[i])

    def remove_all(self):
        """
        Remove all elements in list.
        :return:
        """
        curr = self.head
        self.head = None
        while curr is not None:
            n = curr.next
            curr = None
            curr = n
        self.num = 0

    def push(self, data):
        """
        Push element at head.
        :param data:
        :return:
        """
        node = _Node(data)
        node.next = self.head
        self.head = node
        self.num += 1

    def pop(self, idx=None):
        """
        Pop the Nth element.
        :param idx:
        :return:
        """
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
        """
        Find if a element exist in list.
        :param x:
        :return:
        """
        cur = self.head
        while cur is not None:
            if cur.data == x:
                return True
            cur = cur.next
        return False

    def get_from_end(self, idx):
        """
        Get the Nth element from end.
        :param idx:
        :return:
        """
        if idx >= self.num:
            raise Exception("Out of Index Boundary Exception")
        idx = self.num - idx
        return self.get(idx)

    def get(self, idx):
        """
        Get the Nth element.
        :param idx:
        :return:
        """
        cur = self.head
        for i in range(idx):
            if cur:
                cur = cur.next
            else:
                break
        if cur:
            return cur.data
        return None

    def get_mid(self):
        """
        Get the middle element in list.
        :return:
        """
        if self.empty():
            return None
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def count(self, data):
        """
        Count the number of occurrences a given int in linked list.
        :param data:
        :return:
        """
        if self.empty():
            return 0
        return self._occurrence(self.head, data)

    def _occurrence(self, node, data):
        if not node:
            return 0
        c = self._occurrence(node.next, data)
        if node.data == data:
            c += 1
        return c

    def traverse(self):
        """
        Print all elements.
        :return:
        """
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def size(self):
        return self.num

    def empty(self):
        return self.size() == 0


if __name__ == '__main__':
    l = LinedList()
    l.add_all([0, 1, 2, 3, 4, 5, 6])
    print(l.exist(1))
    print(l.exist(10))
    print(l.get(2))
    print(l.get_from_end(2))
    print(l.get_mid())
    l.append(7)
    print(l.get_mid())
    l.traverse()
    print(l.pop(2))
    print(l.pop())
    l.traverse()
    l.remove_all()
