from base_linked_list import _Node, LinkedList


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
            return i - j
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
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = None
        else:
            cur = cur.next


def remove_duplicate_using_hash(node):
    """
    Traverse the list and push to a hash table if it's not exists, else remove the node.
    :param node:
    :return:
    """
    if not node or not node.next:
        return
    h = set()
    cur = node
    h.add(cur.data)
    while cur.next:
        if cur.next.data not in h:
            h.add(cur.next.data)
            cur = cur.next
        else:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = None


def remove_duplicate_unsorted(node):
    """
    Remove duplicates from a unsorted linked list.
    :param node:
    :return:
    """
    if not node:
        return
    i = node
    while i:
        j = i
        while j.next:
            if j.next.data == i.data:
                tmp = j.next
                j.next = tmp.next
                tmp.next = None
            else:
                j = j.next
        i = i.next


def remove_duplicate_unsorted_merge_sort(node):
    """
    First sort the list using merge sort, Second remove duplicate from a sorted list.
    :param node:
    :return:
    """
    remove_duplicate(merge_sort(node))


def merge_sort(node):
    """
    sort linked list.
    :param node:
    :return:
    """
    if not node or not node.next:
        return node
    mid = middle(node)
    n = mid.next
    mid.next = None
    left = merge_sort(node)
    right = merge_sort(n)
    node = merge(left, right)
    return node


def middle(node):
    """
    需保证向下取整
    :param node:
    :return:
    """
    fast, slow = node.next, node
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
    return slow


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    res = None
    if left.data > right.data:
        res = right
        n = right.next
        right.next = None
        res.next = merge(left, n)
    else:
        res = left
        n = left.next
        left.next = None
        res.next = merge(n, right)
    return res


def swap_node(head, x, y):
    """
    Swapping nodes in a linked list without swapping data.
    :param head:
    :param x:
    :param y:
    :return:
    """
    if x == y:
        return
    prevX = None
    curX = head
    while curX:
        if curX.data == x:
            break
        prevX = curX
        curX = curX.next
    prevY = None
    curY = head
    while curY:
        if curY.data == y:
            break
        prevY = curY
        curY = curY.next
    if not curX:
        return
    if not curY:
        return

    if prevX:
        prevX.next = curY
    else:
        head = curY
    if prevY:
        prevY.next = curX
    else:
        head = curX
    tmp = curX.next
    curX.next = curY.next
    curY.next = tmp
    return head


def pairwise_swap(head):
    """
    Pairwise swap nodes of linked list.
    :param head:
    :return:
    """
    prev = None
    cur = head
    while cur and cur.next:
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = cur
        if not prev:
            head = tmp
        else:
            prev.next = tmp
        prev = cur
        cur = cur.next
    return head


def intersection_sorted(node1, node2):
    """
    Intersection of two sorted linked list.
    :param node1:
    :param node2:
    :return:
    """
    i = node1
    j = node2
    dummy = _Node()
    tail = dummy
    while i and j:
        if i.data == j.data:
            node = _Node(i.data)
            tail.next = node
            tail = node
            i = i.next
            j = j.next
        elif i.data > j.data:
            j = j.next
        else:
            i = i.next
    return dummy.next


def get_intersection_of_two_list(node1, node2):
    """
    Find the intersection point of two linked list.
    :param node1:
    :param node2:
    :return:
    """
    x = y = 0
    cur = node1
    while cur:
        cur = cur.next
        x += 1
    cur = node2
    while cur:
        cur = cur.next
        y += 1
    d = abs(x - y)
    cur1 = node1 if x > y else node2
    cur2 = node1 if x < y else node2
    while d:
        cur1 = cur1.next
        d -= 1
    while cur1 and cur2:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next


def quick_sort(node):
    """
    Sort a linked list using quick sort. 9, 3, 10, 6, 8, 7
    :param node:
    :return:
    """
    return quick_sort_util(node, get_tail(node))


def get_tail(node):
    if not node and not node.next:
        return node
    while node.next:
        node = node.next
    return node


def quick_sort_util(head, tail):
    if not head or head == tail:
        return head
    head, pivot, tail = partition(head, tail)
    if head != pivot:
        cur = head
        while cur.next != pivot:
            cur = cur.next
        cur.next = None
        head = quick_sort_util(head, cur)
        get_tail(head).next = pivot
    pivot.next = quick_sort_util(pivot.next, tail)
    return head


def partition(head, tail):
    prev = None
    pivot = tail
    cur = head
    while cur != pivot:
        if cur.data > pivot.data:
            if not prev:
                head = cur.next
            else:
                prev.next = cur.next
            tmp = cur.next
            tail.next = cur
            tail = cur
            cur.next = None
            cur = tmp
        else:
            prev = cur
            cur = cur.next
    return head, pivot, tail


def segragate_even_odd(node):
    """
    Segregate even and odd nodes in a linked list.
    :param node:
    :return:
    """
    cur = node
    tail = node.tail()
    end = tail
    prev = None
    while cur != end:
        if cur.data & 1:
            if prev:
                prev.next = cur.next
            else:
                node = cur.next
            tmp = cur.next
            tail.next = cur
            tail = cur
            cur.next = None
            cur = tmp
        else:
            prev = cur
            cur = cur.next
    if end.data & 1:
        tail.next = end
        if prev:
            prev.next = end.next
        else:
            node = end.next
        end.next = None
    return node


def reverse_list(node):
    """
    Reverse a linked list.
    :param node:
    :return:
    """
    newhead = get_tail(node)
    reverse_list_util(node)
    return newhead


def reverse_list_util(node):
    if node and node.next:
        n = reverse_list_util(node.next)
        n.next = node
        node.next = None
    return node


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
    dup = _Node()
    dup.add_all([1, 2, 2, 3, 4, 4, 4, 5, 7, 7])
    dup.traverse()
    remove_duplicate(dup)
    dup.traverse()
    unsorted = _Node()
    unsorted.add_all([10, 12, 11, 11, 12, 11, 10])
    unsorted.traverse()
    remove_duplicate_unsorted(unsorted)
    unsorted.traverse()

    un = _Node()
    un.add_all([10, 12, 11, 11, 12, 11, 10])
    remove_duplicate_unsorted_merge_sort(un)
    un.traverse()

    un = _Node()
    un.add_all([10, 12, 11, 11, 12, 11, 10])
    remove_duplicate_using_hash(un)
    un.traverse()

    h = _Node()
    h.add_all([1, 2, 3, 4, 5])
    h = swap_node(h, 1, 4)
    h.traverse()

    h = _Node()
    h.add_all([1, 2, 3, 4, 5])
    pairwise_swap(h).traverse()

    l = LinkedList()
    l.add_all([1, 2, 3, 4, 5])
    l.swap(0, l.size() - 1)
    l.traverse()

    node1 = _Node()
    node1.add_all([1, 2, 3, 4, 5, 10])
    node2 = _Node()
    node2.add_all([3, 4, 8, 10])
    sec = intersection_sorted(node1, node2)
    if sec:
        sec.traverse()
    c = _Node()
    c.add_all([15, 30])
    node1 = _Node()
    node1.add_all([3, 6, 9]).next = c
    node2 = _Node(10)
    node2.next = c
    print(get_intersection_of_two_list(node1, node2))

    n = _Node()
    d = [9, 3, 10, 6, 8, 7]
    d = [1, 2, 3, 4, 5]
    d = [5, 4, 3, 2, 1]
    d = [30, 3, 4, 20, 5]
    n.add_all(d)
    quick_sort(n).traverse()

    n = _Node()
    d = [1, 2, 3, 4, 5, 6]
    # d = [1, 3, 5]
    # d = [2, 4, 6]
    d = [1, 2, 3, 4, 5]
    d = [1, 2]
    n.add_all(d)
    # n = segragate_even_odd(n)
    n = reverse_list(n)
    n.traverse()
