from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, k, v, left=None, right=None):
        self.v = v
        self.k = k
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v

    def __str__(self):
        return self.k + ',' + str(self.v)


class HuffmanCode:
    def __init__(self, x):
        self.arr = []
        for e in x:
            self.arr.append(Node(e[0], e[1]))
        heapify(self.arr)

    def build_tree(self):
        while len(self.arr) > 1:
            n1 = heappop(self.arr)
            n2 = heappop(self.arr)
            if n1.v < n2.v:
                n = Node(None, n1.v + n2.v, n1, n2)
            else:
                n = Node(None, n1.v + n2.v, n2, n1)
            heappush(self.arr, n)

    def code(self):
        node = self.arr[0]
        self.traversal_tree(node, '')

    def traversal_tree(self, node, s):
        if node.left is None and node.right is None:
            print(s, node.k, node.v)
            return
        self.traversal_tree(node.left, s + '0')
        self.traversal_tree(node.right, s + '1')


if __name__ == '__main__':
    arr = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    huffman = HuffmanCode(arr)
    huffman.build_tree()
    huffman.code()
