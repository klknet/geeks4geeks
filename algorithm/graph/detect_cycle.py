"""
Detect Cycle in a Directed Graph.
"""
from algorithm.graph.graph import Graph


def dfs(graph):
    visited = [0] * graph.size()
    recStack = [0] * graph.size()
    for v in range(graph.size()):
        if visited[v] == 0:
            if dfs_util(graph, visited, recStack, v):
                return True
    return False


def dfs_util(graph, visited, recStack, u):
    visited[u] = 1
    recStack[u] = 1
    print(u, end=' ')
    for v in graph.edge[u]:
        if visited[v] == 0:
            dfs_util(graph, visited, recStack, v)
        elif recStack[v] == 1:
            return True
    recStack[u] = 0
    return False


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
print('Have Cycle', dfs(graph))
