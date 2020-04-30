from datastructure.linkedlist.linked_list import _Node, LinedList


def detect_loop(node):
    """
    Detect loop in a linked list.
    :param node:
    :return:
    """
    fast = slow = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def find_length_of_loop(node):
    """
    Find length of loop in linked list.
    :param node:
    :return:
    """
    slow = fast = node
    i = j = 0
    while fast and fast.next:
        fast = fast.next.next
        i += 2
        j += 1
        slow = slow.next
        if fast == slow:
            return i-j
    return 0


def check_palindrome(ll):
    s = []
    cur = ll.head
    while cur:
        s.append(cur.data)
        cur = cur.next
    cur = ll.head
    while cur:
        if cur.data != s.pop():
            return False
        cur = cur.next
    return True


if __name__ == '__main__':
    e = _Node(5)
    d = _Node(4, e)
    c = _Node(3, d)
    b = _Node(2, c)
    a = _Node(1, b)
    e.next = b
    print(detect_loop(a))
    print(find_length_of_loop(a))
    ll = LinedList()
    ll.add_all([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print(check_palindrome(ll))
