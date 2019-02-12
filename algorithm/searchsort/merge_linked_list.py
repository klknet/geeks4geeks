class LinkedList:
    """
    Merge sort for linked list
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = LinkedList.Node(data, self.head)

    def merge_sort(self, node):
        if node is None or node.next is None:
            return node
        mid = self._middle(node)
        mid_of_next = mid.next
        mid.next = None
        left = self.merge_sort(node)
        right = self.merge_sort(mid_of_next)
        sorted_list = self.sort_list(left, right)
        return sorted_list

    def sort_list(self, left, right):
        res = None
        if left is None:
            return right
        if right is None:
            return left
        if left.v > right.v:
            res = right
            res.next = self.sort_list(left, right.next)
        else:
            res = left
            res.next = self.sort_list(left.next, right)
        return res

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.v, end=' ')
            node = node.next
        print()

    def _middle(self, node):
        fast_ptr, slow_ptr = node.next, node
        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
                slow_ptr = slow_ptr.next
        return slow_ptr

    class Node:
        def __init__(self, v, node):
            self.v = v
            self.next = node

        def __str__(self):
            return self.v


if __name__ == '__main__':
    l = LinkedList()
    l.push(15)
    l.push(10)
    l.push(5)
    l.push(3)
    l.push(20)
    l.push(3)
    l.push(2)
    l.push(25)
    l.print_list()
    l.head = l.merge_sort(l.head)
    l.print_list()
