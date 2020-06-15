import random
from base_linked_list import _Node


class Node(object):
    """
    A node have levels.
    """

    def __init__(self, key=None, lv=None):
        self.key = key
        self.lv = lv
        self.forword = [None]*(lv+1)


class SkipList(object):
    def __init__(self, P, MAX_LV):
        self.P = P
        self.MAX_LV = MAX_LV
        self.head = Node(lv=MAX_LV)
        self.level = 0  # skiplist's current level.

    def insert(self, key):
        update = [None]*(self.MAX_LV+1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forword[i] and cur.forword[i].key < key:
                cur = cur.forword[i]
            update[i] = cur
        cur = update[i].forword[0]
        if True or cur is None or cur.key != key:
            lv = self.randomLevel()
            if lv > self.level:
                for i in range(self.level+1, lv+1):
                    update[i] = self.head
                self.level = lv
            n = Node(key, lv)
            for i in range(lv+1):
                n.forword[i] = update[i].forword[i]
                update[i].forword[i] = n

    def delete(self, key):
        update = [None]*(self.MAX_LV+1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forword[i] and cur.forword[i].key < key:
                cur = cur.forword[i]
            update[i] = cur
        cur = cur.forword[0]
        if cur:
            for i in range(cur.lv+1):
                update[i].forword[i] = cur.forword[i]
            del cur

    def search(self, key) -> Node:
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forword[i] and cur.forword[i].key < key:
                cur = cur.forword[i]
        cur = cur.forword[0]
        if cur and cur.key == key:
            print('Fount key %s' % (key))
        else:
            print("Key Not Found %s" % (key))
        return cur

    def display(self):
        for i in range(self.MAX_LV+1):
            cur = self.head.forword[i]
            while cur:
                print(cur.key, end=" ")
                cur = cur.forword[i]
            print()

    def randomLevel(self):
        lv = 0
        while random.random() < self.P and lv < self.MAX_LV:
            lv += 1
        return lv


def max_sum(list1: _Node, list2: _Node) -> _Node:
    """
    Construct a maximum sum linked list out of two sorted linked lists having common nodes.
    """
    if not list1:
        return list2
    if not list2:
        return list1
    cur1, cur2 = list1, list2
    sum1 = sum2 = 0
    head = None
    while cur1 and cur2 and cur1.data != cur2.data:
        if cur1.data<cur2.data:
            sum1 += cur1.data
            cur1 = cur1.next
        else:
            sum2 += cur2.data
            cur2 = cur2.next
    if cur1 is None:
        while cur2:
            sum2 += cur2.data
            cur2 = cur2.next
    if cur2 is None:
        while cur1:
            sum1 += cur1.data
            cur1 = cur1.next
    if sum1>sum2:
        head = list1
        if cur1:
            cur1.next = max_sum(cur1.next if cur1 else None, cur2.next if cur2 else None)
            cur2.next = None
    else:
        head = list2
        if cur2:
            cur2.next = max_sum(cur1.next if cur1 else None, cur2.next if cur2 else None)
            cur1.next = None
    return head


if __name__ == '__main__':
    sl = SkipList(0.5, 3)
    sl.insert(3)
    sl.insert(6)
    sl.insert(18)
    sl.insert(9)
    sl.insert(12)
    sl.insert(19)
    sl.insert(17)
    sl.insert(26)
    sl.insert(21)
    sl.insert(25)
    sl.display()
    sl.search(12)
    sl.search(120)
    sl.delete(17)
    sl.delete(21)
    sl.display()
    list1 = _Node()
    list2 = _Node()
    list1.add_all([1, 3, 30, 90, 120, 240, 511])
    list2.add_all([0, 3, 12, 32, 90, 125, 240, 249])
    print('===========')
    max_sum(list1, list2).traverse()
