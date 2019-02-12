# Merge sort for doubly link list
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, v):
        node = Node(v, None, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def merge_sort(self, temp_head):
        if temp_head is None or temp_head.next is None:
            return temp_head
        second = self.split(temp_head)
        temp_head = self.merge_sort(temp_head)
        second = self.merge_sort(second)
        return self.merge(temp_head, second)

    # Select the smaller node of the two nodes, place the node as first node, recursive do tail either of is none
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.v < second.v:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    def split(self, node):
        slow = fast = node
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

    def print_list(self, node):
        temp = node
        # Forward traversal using next pointers
        while node is not None:
            print(node.v, end=' ')
            temp = node
            node = node.next
        print()
        while temp is not None:
            print(temp.v, end=' ')
            temp = temp.prev
        print()


class Node:
    def __init__(self, v, prev, next):
        self.v = v
        self.prev = prev
        self.next = next


if __name__ == '__main__':
    l = LinkedList()
    l.push(12)
    l.push(14)
    l.push(10)
    l.push(18)
    l.push(2)
    l.print_list(l.head)
    l.head = l.merge_sort(l.head)
    l.print_list(l.head)
