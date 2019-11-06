"""
Transitive closure of a graph.

"""
from algorithm.graph.graph import DirectedWeightMatrixGraph
import sys

INF = sys.maxsize


def transitive(graph):
    reach = [[0 for col in range(graph.size())] for row in range(graph.size())]
    for k in range(graph.size()):
        for i in range(graph.size()):
            for j in range(graph.size()):
                reach[i][j] = reach[i][j] | (graph.matrix[i][k] & graph.matrix[k][j])
    print(reach)


matrix = [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
g1 = DirectedWeightMatrixGraph(matrix)
transitive(g1)
