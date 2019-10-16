"""
Prim's minimum spanning tree.
"""
import sys
from algorithm.graph.graph import UndirectedWeightGraph


def prim_mst(graph, s):
    mst_set = [False] * graph.size()
    parent = [-1] * graph.size()
    key = [sys.maxsize] * graph.size()
    key[s] = 0
    for c in range(graph.size()):
        u = minKey(mst_set, key)
        mst_set[u] = True
        for v, w in graph.graph[u]:
            if not mst_set[v] and key[v] > w:
                key[v] = w
                parent[v] = (u, w)
    print_mst(parent, s)


def print_mst(parent, s):
    for i in range(len(parent)):
        if i != s:
            print(parent[i][0], '-->', i, '=', parent[i][1])


def minKey(mst_set, key):
    m = sys.maxsize
    min_v = -1
    for v in range(len(key)):
        if not mst_set[v] and key[v] < m:
            m = key[v]
            min_v = v
    return min_v


graph = UndirectedWeightGraph()
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(1, 2, 8)
graph.add_edge(2, 8, 2)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 5, 10)
graph.add_edge(6, 5, 2)
graph.add_edge(7, 8, 7)
graph.add_edge(7, 6, 1)
graph.add_edge(8, 6, 6)

prim_mst(graph, 0)


print()

g1 = UndirectedWeightGraph()
g1.add_edge(0, 1, 2)
g1.add_edge(0, 3, 6)
g1.add_edge(1, 2, 3)
g1.add_edge(1, 3, 8)
g1.add_edge(1, 4, 5)
g1.add_edge(2, 4, 7)
g1.add_edge(3, 4, 9)
prim_mst(g1, 0)
