"""
Hamiltonian Cycle.
"""
from algorithm.graph.graph import UndirectedMatrixGraph


def hamiltonian_cycle(graph, s):
    path = [False] * graph.size()
    path[s] = True
    res = [s]
    num = 1
    flag = False
    for v in range(graph.size()):
        if s != v and graph.matrix[s][v] == 1:
            if hamil_util(graph, s, v, path, num, res):
                flag = True
                break
    if flag:
        print(res)
    else:
        print("no Hamiltonian Cycle")


def hamil_util(graph, s, u, path, num, res):
    path[u] = True
    res.append(u)
    if num == graph.size()-1:
        if graph.matrix[u][s] == 1:
            return True
        else:
            return False
    for v in range(graph.size()):
        if graph.matrix[u][v] == 1 and not path[v] and s != v:
            if hamil_util(graph, s, v, path, num + 1, res):
                return True
    path[u] = False
    res.pop()
    return False


matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
g = UndirectedMatrixGraph(matrix)
hamiltonian_cycle(g, 0)

matrix1 = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]
g1 = UndirectedMatrixGraph(matrix1)
hamiltonian_cycle(g1, 0)
