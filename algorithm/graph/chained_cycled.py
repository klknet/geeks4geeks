"""
Find if an array of strings can be chained to form a cycle.
"""
from algorithm.graph.graph import DirectedWeightMatrixGraph


def can_be_chained(arr):
    matrix = [[0 for col in range(26)] for row in range(26)]
    graph = DirectedWeightMatrixGraph(matrix)
    vertex = set()
    for s in arr:
        start = ord(s[0]) - ord('a')
        end = ord(s[-1]) - ord('a')
        vertex.add(start)
        vertex.add(end)
        matrix[start][end] = 1
    return is_euler_cycle(graph, vertex)


def is_euler_cycle(graph, vertex):
    if not is_sc(graph, vertex):
        return False
    if not is_sc(get_transpose(graph), vertex):
        return False
    for u in range(graph.size()):
        indegree = 0
        outdegree = 0
        for i in range(graph.size()):
            if graph.matrix[u][i] == 1:
                outdegree += 1
            if graph.matrix[i][u] == 1:
                indegree += 1
        if indegree != outdegree:
            return False
    return True


def is_sc(graph, vertex):
    visited = [False] * graph.size()
    r = vertex.pop()
    dfs_util(graph, r, visited)
    vertex.add(r)
    for v in vertex:
        if not visited[v]:
            return False
    return True


def dfs_util(graph, u, visited):
    visited[u] = True
    for v in range(graph.size()):
        if not visited[v] and graph.matrix[u][v] == 1:
            dfs_util(graph, v, visited)


def get_transpose(graph):
    t_matrix = [[0 for col in range(26)] for row in range(26)]
    for i in range(26):
        for j in range(26):
            t_matrix[j][i] = graph.matrix[i][j]
    t_graph = DirectedWeightMatrixGraph(t_matrix)
    return t_graph


print(can_be_chained(["for", "geek", "rig", "kaf"]))
print(can_be_chained(["aab", "abb"]))
