"""
Compare numbers represented by linked list.
"""
from datastructure.linkedlist.base_linked_list import LinkedList


def compare(list1, list2):
    remove_leading_zero(list1)
    remove_leading_zero(list2)
    n1, n2 = list1.size(), list2.size()
    if n1 != n2:
        return 1 if n1 > n2 else -1
    cur1, cur2 = list1.head, list2.head
    while cur1:
        if cur1.data == cur2.data:
            cur1 = cur1.next
            cur2 = cur2.next
        else:
            return 1 if cur1.data > cur2.data else -1
    return 0


def remove_leading_zero(linkedlist):
    cur = linkedlist.head
    while cur:
        if cur.data == 0:
            cur = cur.next
            linkedlist.num -= 1
        else:
            break
    if cur != linkedlist.head:
        linkedlist.head = cur


list1 = LinkedList()
list1.add_all([0, 0, 1, 2, 4])
list2 = LinkedList()
list2.add_all([0, 0, 0, 4, 2])
print(compare(list1, list2))

list3 = LinkedList()
list3.add_all([2, 3, 1, 2, 4])
list4 = LinkedList()
list4.add_all([2, 3, 2, 4, 2])
print(compare(list3, list4))
