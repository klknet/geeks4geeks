"""
Fleury's Algorithm for printing Eulerian Cycle or Path.
"""
from algorithm.graph.graph import UndirectedGraph


def fleury_alg(graph):
    i = 0
    for i in range(graph.size()):
        if len(graph.graph[i]) & 1:
            break
    if i == graph.size():
        i = 0
    res = []
    visited = [False] * graph.size()
    print_euler(graph, i, res, visited)
    print(res)


def print_euler(graph, u, res, visited):
    for v in graph.graph[u]:
        if is_valid_edge(graph, u, v, visited):
            res.append((u, v))
            rmv_edge(graph, u, v)
            print_euler(graph, v, res, visited)


def rmv_edge(graph, u, v):
    graph.graph[u].remove(v)
    graph.graph[v].remove(u)


def is_valid_edge(graph, u, v, visited):
    if len(graph.graph[u]) == 1:
        return True
    bef = dfs_count(graph, u, visited)
    rmv_edge(graph, u, v)
    reset_visited(visited)
    aft = dfs_count(graph, u, visited)
    reset_visited(visited)
    graph.add_edge(u, v)
    if bef > aft:
        return False
    return True


def reset_visited(visited):
    for i in range(len(visited)):
        visited[i] = False


def dfs_count(graph, u, visited):
    visited[u] = True
    count = 0
    for v in graph.graph[u]:
        if not visited[v]:
            count = dfs_count(graph, v, visited) + 1
    return count


g1 = UndirectedGraph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
fleury_alg(g1)

g2 = UndirectedGraph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 0)
fleury_alg(g2)

g3 = UndirectedGraph()
g3.add_edge(1, 0)
g3.add_edge(0, 2)
g3.add_edge(2, 1)
g3.add_edge(0, 3)
g3.add_edge(3, 4)
g3.add_edge(3, 2)
g3.add_edge(3, 1)
g3.add_edge(2, 4)
fleury_alg(g3)
