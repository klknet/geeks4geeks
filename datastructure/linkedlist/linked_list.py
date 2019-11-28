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
        for i in range(len(arr)-1, 0, -1):
            self.add_node(arr[i])

    def size(self):
        return self.num
