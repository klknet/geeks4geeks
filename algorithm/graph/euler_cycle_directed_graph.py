"""
Euler Cycle in a directed graph.
"""
from algorithm.graph.graph import DirectedGraph


def euler_cycle(graph):
    if not is_sc(graph):
        return False
    tran = get_transpose(graph)
    if not is_sc(tran):
        return False
    for v in range(graph.size()):
        if len(graph.graph[v]) != len(tran.graph[v]):
            return False
    return True


def get_transpose(graph):
    g = DirectedGraph()
    for u in range(graph.size()):
        for v in graph.graph[u]:
            g.add_edge(v, u)
    return g


def is_sc(graph):
    visited = [False] * graph.size()
    dfs_util(graph, 0, visited)
    for v in visited:
        if not v:
            return False
    return True


def dfs_util(graph, u, visited):
    visited[u] = True
    for v in graph.graph[u]:
        if not visited[v]:
            dfs_util(graph, v, visited)


g = DirectedGraph()
g.add_edge(1,0)
g.add_edge(0,2)
g.add_edge(2,1)
g.add_edge(0,3)
g.add_edge(3,4)
g.add_edge(4,0)
print(euler_cycle(g))