class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data


class BinaryTree:
    def __init__(self, node):
        self.head = node

    def bfs(self):
        queue = [self.head]
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                size -= 1
                node = queue.pop()
                print(node.data, end=" ")
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            print("换行")


node3 = Node(Node(data=6), Node(data=7), 3)
node2 = Node(Node(data=4), Node(data=5), 2)
node = Node(node2, node3, 1)
bt = BinaryTree(node)
bt.bfs()



