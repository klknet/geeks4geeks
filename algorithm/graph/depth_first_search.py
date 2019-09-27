"""
Depth first search for a graph.
"""
from algorithm.graph.graph import Graph


def dfs(graph, start):
    visited = [0] * graph.size()
    dfs_util(graph, visited, start)


def dfs_util(graph, visited, u):
    visited[u] = 1
    print(u, end=' ')
    for v in graph.edge[u]:
        if visited[v] == 0:
            dfs_util(graph, visited, v)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
dfs(graph, 2)
