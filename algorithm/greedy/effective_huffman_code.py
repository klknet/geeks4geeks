from algorithm.greedy.huffman_code import Node


class HuffmanCode:
    def __init__(self, arr):
        self.q1 = []
        self.q2 = []
        for e in arr:
            self.q1.append(Node(e[0], e[1]))

    def build_tree(self):
        while len(self.q1) > 0 or len(self.q2) != 1:
            n1 = self.fetch_node()
            n2 = self.fetch_node()
            if n1 > n2:
                n = Node(None, n1.v + n2.v, n2, n1)
            else:
                n = Node(None, n1.v + n2.v, n1, n2)
            self.q2.append(n)

    def fetch_node(self):
        """ return the smaller of the two queues """
        if len(self.q1) == 0:
            return self.q2.pop(0)
        elif len(self.q2) == 0:
            return self.q1.pop(0)
        else:
            if self.q1[0] > self.q2[0]:
                return self.q2.pop(0)
            else:
                return self.q1.pop(0)

    def print_tree(self):
        node = self.q2[0]
        self.recur_traversal(node, '')

    def recur_traversal(self, node, s):
        if node.left is not None:
            self.recur_traversal(node.left, s + '0')
        if node.right is not None:
            self.recur_traversal(node.right, s + '1')
        if node.left is None and node.right is None:
            print(s, node)


arr = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
huffman = HuffmanCode(arr)
huffman.build_tree()
huffman.print_tree()
