"""
Floyd Warshall shortest path tree.
"""
from algorithm.graph.graph import DirectedWeightMatrixGraph
import sys

INF = sys.maxsize


def floyd_warshall(graph):
    V = graph.size()
    spt = [[0 for col in range(V)] for row in range(V)]
    for i in range(V):
        for j in range(V):
            spt[i][j] = graph.matrix[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph.matrix[i][j] != 0 and spt[i][k] != INF and spt[k][j] != INF \
                        and spt[i][j] > spt[i][k] + spt[k][j]:
                    spt[i][j] = spt[i][k] + spt[k][j]

    print_spt(spt)


def print_spt(spt):
    for i in range(len(spt[0])):
        for j in range(len(spt[0])):
            if i != j and spt[i][j] != INF:
                print(i, '-->', j, spt[i][j])


matrix = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
graph = DirectedWeightMatrixGraph(matrix)
floyd_warshall(graph)
