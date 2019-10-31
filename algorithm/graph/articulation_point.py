"""
Articulation Points in a graph.
"""
from algorithm.graph.graph import UndirectedGraph
time = 0


def articulation_point(graph):
    ap = [False] * graph.size()
    disc = [-1] * graph.size()
    low = [-1] * graph.size()
    parent = [-1] * graph.size()
    visited = [False] * graph.size()
    for u in range(graph.size()):
        if not visited[u]:
            dfs_util(graph, u, visited, disc, low, parent, ap)
    for i in range(graph.size()):
        if ap[i]:
            print(i, end=' ')
    print()


def dfs_util(graph, u, visited, disc, low, parent, ap):
    global time
    visited[u] = True
    disc[u] = time
    low[u] = time
    time += 1
    children = 0
    for v in graph.graph[u]:
        if not visited[v]:
            children += 1
            parent[v] = u
            dfs_util(graph, v, visited, disc, low, parent, ap)
            low[u] = min(low[u], low[v])
            # case 1, u is root of dfs tree and has two or more children.
            if parent[u] == -1 and children > 1:
                ap[u] = True
            # case 2, if u is not root and low value of one of its children is more than discovery time of u.
            if parent[u] != -1 and disc[u] <= low[v]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


g1 = UndirectedGraph()
g1.add_edge(1,0)
g1.add_edge(0,2)
g1.add_edge(2,1)
g1.add_edge(0,3)
g1.add_edge(3,4)
articulation_point(g1)

g2 = UndirectedGraph()
g2.add_edge(0,1)
g2.add_edge(1,2)
g2.add_edge(2,3)
articulation_point(g2)

g3 = UndirectedGraph()
g3.add_edge(0,1)
g3.add_edge(1,2)
g3.add_edge(2,0)
g3.add_edge(1,3)
g3.add_edge(1,4)
g3.add_edge(1,6)
g3.add_edge(1,6)
g3.add_edge(3,5)
g3.add_edge(4,5)
articulation_point(g3)