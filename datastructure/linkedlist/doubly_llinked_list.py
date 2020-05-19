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

    def valueOf(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                break
            cur = cur.next
        return cur

    def traverse(self):
        self.head.traverse()

    def tail(self):
        cur = self.head
        while cur:
            if not cur.next:
                break
            cur = cur.next
        return cur


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.push(1)
    d.push(2)
    d.append(3)
    d.append(6)
    d.insertAfter(d.valueOf(3), 5)
    d.insertAfter(d.valueOf(6), 7)
    d.insertAfter(d.valueOf(1), 7)
    d.insertAfter(d.valueOf(10), 7)
    d.traverse()
