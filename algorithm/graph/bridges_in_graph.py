"""
Bridges in a graph.
"""
from algorithm.graph.graph import UndirectedGraph

time=0

def find_bridge(graph):
    res = []
    visited = [False] * graph.size()
    disc = [-1] * graph.size()
    low = [-1] * graph.size()
    parent = [-1] * graph.size()
    for u in range(graph.size()):
        if not visited[u]:
            dfs_util(graph, visited, u, disc, low, parent, res)
    print(res)


def dfs_util(graph, visited, u, disc, low, parent, res):
    global time
    visited[u] = True
    disc[u] = time
    low[u] = time
    time += 1
    for v in graph.graph[u]:
        if not visited[v]:
            parent[v] = u
            dfs_util(graph, visited, v, disc, low, parent, res)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                res.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


g1 = UndirectedGraph()
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
find_bridge(g1)

g2 = UndirectedGraph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
find_bridge(g2)

g3 = UndirectedGraph()
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)
find_bridge(g3)


