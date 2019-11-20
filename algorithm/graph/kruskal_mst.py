"""
Kruskal's minimum spanning tree.
"""
from algorithm.graph.graph import UndirectedWeightGraph, DisjointSet


def kruskal_mst(graph):
    graph.edge.sort(key = lambda x: x[2])
    disjoint = DisjointSet(graph.size())
    c = 0
    res = []
    for u, v, w in graph.edge:
        u_p = disjoint.find(u)
        v_p = disjoint.find(v)
        if u_p != v_p:
            disjoint.union(u, v)
            res.append((u, v, w))
            c += 1

    if c == graph.size()-1:
        return res
    return None



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
res = kruskal_mst(graph)
if res != None:
    for u, v, w in res:
        print(u, '-->', v, w)

