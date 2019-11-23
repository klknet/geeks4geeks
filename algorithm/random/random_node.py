"""
Select a random node from a singly linked list.
"""
import random


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def random_node(self):
        current = self.head
        n = 2
        result = current.data
        while current.next:
            current = current.next
            r = random.randrange(n)
            if r == 0:
                result = current.data
            n += 1
        return result

    def size(self):
        n = 0
        tmp = self.head
        while tmp:
            n += 1
            tmp = tmp.next
        return n


list = LinkedList()
list.insert_node(1)
list.insert_node(2)
list.insert_node(3)
list.insert_node(4)
list.insert_node(5)
list.insert_node(6)
list.insert_node(7)
list.insert_node(8)
print(list.random_node())