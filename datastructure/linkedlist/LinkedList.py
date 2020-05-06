from datastructure.linkedlist.linked_list import _Node, LinkedList


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
    """
    Check a linked list is a palindrome.
    Using stack, first traverse the list and push to stack, second traverse the list, if current node equals to stack's
    element, pop element, if not equal, then the list is not a palindrome linked list.
    :param ll:
    :return:
    """
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


def remove_duplicate(node):
    """
    Remove duplicates from a sorted linked list.
    :param node:
    :return:
    """
    cur = node
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        cur = cur.next


if __name__ == '__main__':
    e = _Node(5)
    d = _Node(4, e)
    c = _Node(3, d)
    b = _Node(2, c)
    a = _Node(1, b)
    e.next = b
    print(detect_loop(a))
    print(find_length_of_loop(a))
    ll = LinkedList()
    ll.add_all([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print(check_palindrome(ll))
    dup = _Node(1)
    dup.add_all([1, 2, 2, 3, 4, 4, 4, 5, 6, 7])
    dup.traverse()
    remove_duplicate(dup)
    dup.traverse()

