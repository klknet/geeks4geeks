"""
Largest Independent Set.
Given a binary tree, find the size of the largest independent set in it. A subset of all tree nodes is an independent set
if there is no edge between any two nodes of the subset.
Let liss(X) be the largest independent subset of tree with root X.
liss(x) = max(1 + sum of liss for all grandchildren of x, sum of liss for all children of x).
The idea is simple, there are two possibilities for every node X, either X is a member of the set or not a member. If X
is a member, then the value of liss(x) is 1 plus sum of liss of all grandchildren. If X is not a member, then the value
is sum of liss of all grandchildren.
"""


def liss(node):
    if node is None:
        return 0
    if node.liss:
        return node.liss
    incl = 0
    if node.left:
        incl += (liss(node.left.left) + liss(node.left.right))
    if node.right:
        incl += (liss(node.right.left) + liss(node.right.right))
    excl = liss(node.left) + liss(node.right)
    node.liss = max(1 + incl, excl)
    return node.liss



class BinaryTree:

    def __init__(self, num):
        self.root = Node(num)
        self.num = 1

    def add_node(self, num):
        if isinstance(num, list):
            for n in num:
                self._recur_add(self.root, Node(n))
                self.num += 1
        elif isinstance(num, int):
            self._recur_add(self.root, Node(num))
            self.num += 1

    def _recur_add(self, parent, node):
        # determine to which branch the node should be added.
        if parent.num > node.num:
            if parent.left is None:
                parent.left = node
            else:
                self._recur_add(parent.left, node)
        else:
            if parent.right is None:
                parent.right = node
            else:
                self._recur_add(parent.right, node)


class Node:
    def __init__(self, num, left=None, right=None):
        self.num = num
        self.liss = 0
        self.left = left
        self.right = right

    @staticmethod
    def traverse(node):
        q = [node]
        while len(q) > 0:
            n = q.pop()
            print(n.num, end=' ')
            if n.left is not None:
                q.insert(0, n.left)
            if n.right is not None:
                q.insert(0, n.right)


tree = BinaryTree(20)
arr = [10, 30, 5, 15, 12, 17, 40]
tree.add_node(arr)
Node.traverse(tree.root)
print(liss(tree.root))
