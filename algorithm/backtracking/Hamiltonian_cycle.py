"""
Hamiltonian Cycle.
Hamiltonian path is an undirected graph is a path that visits each vertices exactly once. A Hamiltonian cycle is a Hamiltonian
path such that there is an edge from the last vertex to the first vertex of the Hamiltonian path.
"""


def hamiltonian_cycle(graph):
    # graph.path[0] = 0
    res = False
    for i in range(graph.v):
        graph.path[0] = i
        res = hamil_util(graph, 1) or res
    # graph.path[0] = 1
    # res = hamil_util(graph, 1) or res
    if not res:
        print("no solution")


def hamil_util(graph, pos):
    if graph.v == pos:
        if graph.matrix[graph.path[pos - 1]][graph.path[0]] == 1:
            graph.print_path()
            return True
        return False
    res = False
    for i in range(graph.v):
        if graph.isSafe(i, pos):
            graph.path[pos] = i
            res = hamil_util(graph, pos + 1) or False
            graph.path[pos] = -1
    return res


class Graph(object):
    def __init__(self, v):
        self.v = v
        self.matrix = [[0 for col in range(v)] for row in range(v)]
        self.path = [-1] * self.v

    def isSafe(self, v, pos):
        if self.matrix[v][self.path[pos - 1]] == 0:
            return False
        for i in range(pos):
            if self.path[i] == v:
                return False
        return True

    def print_path(self):
        print(self.path)


graph = Graph(5)
graph.matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1], [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]]
hamiltonian_cycle(graph)
print("################")
g2 = Graph(5)
"""
(0)--(1)--(2)
 |   / \   |
 |  /   \  |
(3)-------(4)
"""
g2.matrix =  [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0], ]
hamiltonian_cycle(g2)
