class LinkedList:
    def __init__(self):
        self.head = None
        self.sort = None

    def push(self, v):
        node = Node(v, None, self.head)
        self.head.prev = node
        self.head = node

    def merge_sort(self, tempHead):
        if tempHead is None or tempHead.next is None:
            return tempHead
        second = self.split(tempHead)

    def split(self, node):
        slow = fast = node
        while fast is not None:
            fast = fast.next


class Node:
    def __init__(self, v, next):
        self.v = v
        self.next = next



if __name__ == '__main__':
    l = LinkedList()
    l.push(10)
    l.push(5)
    l.push(9)
    l.push(1)
    l.push(18)
    l.push(-88)
    l.print_list()
    l.insert_sort()
    l.print_list()