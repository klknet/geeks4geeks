# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

    def traverse(self):
        cur=self
        while cur:
            print(cur.val,end=' ')
            cur=cur.next
        print()

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1=l1
        cur2=l2
        res = []
        s=c=0
        while cur1 and cur2:
            s=(cur1.val+cur2.val+c)%10
            c=(cur1.val+cur2.val+c)//10
            cur1=cur1.next
            cur2=cur2.next
            res.append(s)
        while cur1:
            s=(cur1.val+c)%10
            c=(cur1.val+c)/10
            cur1=cur1.next
            res.append(s)
        while cur2:
            s=(cur2.val+c)%10
            c=(cur2.val+c)/10
            cur2=cur2.next
            res.append(s)
        if c!=0:
            res.append(c)
        result = ListNode(res[0])
        cur = result
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur=cur.next
        return result

l1=ListNode(2,ListNode(4,ListNode(3)))
l2=ListNode(5,ListNode(6,ListNode(4)))
Solution().addTwoNumbers(l1,l2).traverse()
