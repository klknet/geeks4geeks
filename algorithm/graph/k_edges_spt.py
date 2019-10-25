"""
Shortest path with exactly k edges in a directed and weighted graph.
"""
import sys
from algorithm.graph.graph import DirectedWeightMatrixGraph

INF = sys.maxsize


def spt_with_k_edge(graph, u, v, k):
    if k == 0 and u == v:
        return 0
    if k == 1 and graph.matrix[u][v] != INF:
        return graph.matrix[u][v]
    if k <= 0:
        return INF
    res = INF
    for i in range(graph.size()):
        if graph.matrix[u][i] != INF and u != i and v != i:
            disc = spt_with_k_edge(graph, i, v, k - 1)
            if disc != INF:
                res = min(res, graph.matrix[u][i] + disc)
    return res


def spt_with_k_edge_dp(graph, u, v, k):
    dp = [[[INF for u in range(k+1)] for j in range(graph.size())] for i in range(graph.size())]
    for e in range(k+1):
        for i in range(graph.size()):
            for j in range(graph.size()):
                if e == 0 and i == j:
                    dp[i][j][e] = 0
                if e == 1 and graph.matrix[i][j] != INF:
                    dp[i][j][e] = graph.matrix[i][j]
                if e>1:
                    for a in range(graph.size()):
                        if graph.matrix[i][a] != INF and a != i and a != j and dp[a][j][e-1] != INF:
                            dp[i][j][e] = min(dp[i][j][e], graph.matrix[i][a]+dp[a][j][e-1])
    return dp[u][v][k]


matrix = [[0, 10, 3, 2],
          [INF, 0, INF, 7],
          [INF, INF, 0, 6],
          [INF, INF, INF, 0]]
graph = DirectedWeightMatrixGraph(matrix)
print(spt_with_k_edge(graph, 0, 3, 2))
print(spt_with_k_edge(graph, 0, 1, 2))
print(spt_with_k_edge(graph, 0, 0, 2))
print(spt_with_k_edge(graph, 0, 0, 0))

print(spt_with_k_edge_dp(graph, 0, 3, 2))
