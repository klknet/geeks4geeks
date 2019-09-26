"""
Depth first search for a graph.
"""
from collections import defaultdict


def dfs(graph, start):
    visited = [0] * graph.vertex
    dfs_util(graph, visited, start)



def dfs_util(graph, visited, u):
    visited[u] = 1
    print(u, end=' ')
    for v in graph.edge[u]:
        if visited[v] == 0:
            dfs_util(graph, visited, v)


class Graph(object):
    def __init__(self, v):
        self.vertex = v
        self.edge = defaultdict(list)

    def add_edge(self, u, v):
        self.edge[u].append(v)


graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
dfs(graph, 2)
