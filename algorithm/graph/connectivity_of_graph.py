"""
Check if a graph is strongly connected.
"""
from algorithm.graph.graph import DirectedGraph


def strongly_connected(graph):
    if not is_connected(graph):
        return False
    if not is_connected(reverse_graph(graph)):
        return False
    return True


def reverse_graph(graph):
    re = DirectedGraph()
    for u in range(graph.size()):
        for v in graph.graph[u]:
            re.add_edge(v, u)
    return re


def is_connected(graph):
    visited = [False] * graph.size()
    dfs_util(graph, visited, 0)

    for v in visited:
        if not v:
            return False
    return True


def dfs_util(graph, visited, u):
    visited[u] = True
    for v in graph.graph[u]:
        if not visited[v]:
            dfs_util(graph, visited, v)


graph = DirectedGraph()
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,0)
graph.add_edge(2,4)
graph.add_edge(4,2)
print(strongly_connected(graph))

graph1 = DirectedGraph()
graph1.add_edge(0,1)
graph1.add_edge(1,2)
graph1.add_edge(2,3)
print(strongly_connected(graph1))