"""
Biconnected Graph.
"""
from algorithm.graph.graph import UndirectedGraph
time = 0


def is_bc(graph):
    visited = [False] * graph.size()
    disc = [-1] * graph.size()
    low = [-1] * graph.size()
    parent = [-1] * graph.size()
    ap = [False] * graph.size()
    dfs_util(graph, 0, visited, disc, low, parent, ap)
    for f in ap:
        if f:
            return False
    for f in visited:
        if not f:
            return False
    return True


def dfs_util(graph, u, visited, disc, low, parent, ap):
    global time
    disc[u] = time
    low[u] = time
    time+=1
    visited[u] = True
    children = 0
    for v in graph.graph[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            dfs_util(graph, v, visited, disc, low, parent, ap)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1:
                ap[u] = True
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


g1 = UndirectedGraph()
g1.add_edge(0, 1)
print(is_bc(g1))

g2 = UndirectedGraph()
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(3, 4)
g2.add_edge(2, 4)
print(is_bc(g2))

g3 = UndirectedGraph()
g3.add_edge(1, 0)
g3.add_edge(0, 2)
g3.add_edge(2, 1)
g3.add_edge(0, 3)
g3.add_edge(3, 4)
print(is_bc(g3))

g4 = UndirectedGraph()
g4.add_edge(1, 0)
g4.add_edge(0, 2)
g4.add_edge(2, 1)
g4.add_edge(0, 3)
g4.add_edge(3, 4)
print(is_bc(g4))

g5 = UndirectedGraph()
g5.add_edge(0, 1)
g5.add_edge(1, 2)
g5.add_edge(2, 0)
print(is_bc(g5))