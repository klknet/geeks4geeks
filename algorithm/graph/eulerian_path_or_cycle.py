"""
Eulerian paht or cycle.
"""

from algorithm.graph.graph import UndirectedGraph


def eulerian_path(graph):
    visited = [False] * graph.size()
    # case 1, graph must be connected.
    if not is_connected(graph, visited):
        return 0
    odd = 0
    for u in range(graph.size()):
        if len(graph.graph[u]) & 1:
            odd += 1
    if odd > 2:
        return 0
    # if odd is 2, then semi-Eulerian, if odd is 0, then Eulerian.
    return 1 if odd == 2 else 2


def is_connected(graph, visited):
    # find a vertex with non-zero degree
    i = 0
    for i in range(graph.size()):
        if len(graph.graph[i]) > 0:
            break
    if i == graph.size():
        return True
    dfs_util(graph, i, visited)
    for u in range(graph.size()):
        if not visited[u] and len(graph[u]) > 0:
            return False
    return True


def dfs_util(graph, u, visited):
    visited[u] = True
    for v in graph.graph[u]:
        if not visited[v]:
            dfs_util(graph, v, visited)


def format(val):
    if val == 0:
        print("have no Eulerian")
    elif val == 1:
        print("have Eulerian Path")
    elif val == 2:
        print("have Eulerian Cycle")


g1 = UndirectedGraph()
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
format(eulerian_path(g1))

g2 = UndirectedGraph()
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(3, 4)
g2.add_edge(4, 0)
format(eulerian_path(g2))

g3 = UndirectedGraph()
g3.add_edge(1, 0)
g3.add_edge(0, 2)
g3.add_edge(2, 1)
g3.add_edge(0, 3)
g3.add_edge(3, 4)
g3.add_edge(1, 3)
format(eulerian_path(g3))

g4 = UndirectedGraph()
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 0)
format(eulerian_path(g4))

g5 = UndirectedGraph()
format(eulerian_path(g5))
