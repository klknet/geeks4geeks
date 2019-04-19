"""
Vertex Cover Problem.
A vertex cover of an undirected graph is a subset of its vertices such that for every edge (u,v) of the graph, either 'u'
or 'v' is in the vertex cover.

The idea is to consider following two possibilities for root and recursively for all nodes down the root.
1)Root is part of vertex cover. In this case, root covers all children edges. We recursively calculate size of vertex
covers for left and right subtrees and add 1 to the result(for root).
2)Root is not part of vertex cover. In this case, both children of root must be included in vertex cover to cover all root
to children edges. We recursively calculate size of vertex covers of all grandchildren and number of children to the
result(for two children of root).
"""


def minimum_vertex_cover(node):
    if node is None:
        return 0
    incl = 1 + minimum_vertex_cover(node.left) + minimum_vertex_cover(node.right)
    excl = 0
    if node.left is not None:
        excl += 1 + minimum_vertex_cover(node.left.left) + minimum_vertex_cover(node.left.right)
    if node.right is not None:
        excl += 1 + minimum_vertex_cover(node.right.left) + minimum_vertex_cover(node.right.right)
    return min(incl, excl)


vertex_cover = []


def min_vertex_cover_dp(node):
    if node is None:
        return 0
    # no edge
    if node.left is None and node.right is None:
        return 0
    if node.num is not None:
        return node.num
    incl = 1 + min_vertex_cover_dp(node.left) + min_vertex_cover_dp(node.right)
    excl = 0
    if node.left is not None:
        excl += 1 + min_vertex_cover_dp(node.left.left) + min_vertex_cover_dp(node.left.right)
    if node.right is not None:
        excl += 1 + min_vertex_cover_dp(node.right.left) + min_vertex_cover_dp(node.right.right)
    node.set_num(min(incl, excl))
    if incl <= excl:
        vertex_cover.append(node.value)
    return node.num


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.num = None

    def set_num(self, num):
        self.num = num


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
print(minimum_vertex_cover(root))
print(min_vertex_cover_dp(root))
print(vertex_cover)
