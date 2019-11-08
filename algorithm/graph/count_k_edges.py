"""
Count all possible walks from a source to a destination with exactly k edges.
"""
from algorithm.graph.graph import DirectedWeightMatrixGraph


def count_k_edegs(graph, s, d, k):
    if k == 0 and s == d:
        return 1
    if k == 1 and graph.matrix[s][d] == 1:
        return 1
    if k <= 0:
        return 0
    c = 0
    for v in range(graph.size()):
        if graph.matrix[s][v] == 1:
            c += count_k_edegs(graph, v, d, k - 1)
    return c


matrix = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
g = DirectedWeightMatrixGraph(matrix)
print(count_k_edegs(g, 0, 3, 2))
