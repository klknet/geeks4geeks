"""
Max flow problem introduction.
"""
import sys

from algorithm.graph.graph import DirectedWeightMatrixGraph

INF = sys.maxsize


def ford_fulkerson_max_flow(graph, s, t):
    rMatrix = [[0 for col in range(graph.size())] for row in range(graph.size())]
    for r in range(graph.size()):
        for c in range(graph.size()):
            rMatrix[r][c] = graph.matrix[r][c]
    # Reverse graph
    rGraph = DirectedWeightMatrixGraph(rMatrix)
    parent = [-1] * graph.size()
    max_flow = 0
    # if exists an augment path.
    while bfs(rGraph, s, t, parent):
        min_flow = INF
        v = t
        # calculate the minimum flow on the path
        while v != s:
            u = parent[v]
            min_flow = min(min_flow, rGraph.matrix[u][v])
            v = u
        max_flow += min_flow
        v = t
        # update original graph edge capacity and reversed graph's capacity.
        while v != s:
            u = parent[v]
            rGraph.matrix[v][u] += min_flow
            rGraph.matrix[u][v] -= min_flow
            v = u
    return max_flow


def bfs(graph, s, t, parent):
    visited = [False] * graph.size()
    queue = [s]
    while len(queue) > 0:
        u = queue.pop()
        visited[u] = True
        for v in range(graph.size()):
            if graph.matrix[u][v] != 0 and not visited[v]:
                queue.append(v)
                parent[v] = u

    return visited[t]


matrix = [[0, 16, 13, 0, 0, 0],
          [0, 0, 10, 12, 0, 0],
          [0, 4, 0, 0, 14, 0],
          [0, 0, 9, 0, 0, 20],
          [0, 0, 0, 7, 0, 4],
          [0, 0, 0, 0, 0, 0]
          ]
g = DirectedWeightMatrixGraph(matrix)
print(ford_fulkerson_max_flow(g, 0, 5))