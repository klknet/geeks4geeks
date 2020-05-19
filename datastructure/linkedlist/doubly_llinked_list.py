from datastructure.linkedlist.base_linked_list import _DoubleNode


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


def reverse(node):
    if not node:
        return
    newhead = reverse(node.next)
    node.prev, node.next = node.next, node.prev
    return newhead if newhead else node


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
    d.reverseTraverse()
