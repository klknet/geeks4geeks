"""
Boruvka's Algorithm.
"""
from algorithm.graph.graph import UndirectedWeightGraph, DisjointSet

def boruvka_mst(graph):
    mstVertex = graph.size()
    disjoint = DisjointSet(mstVertex)
    weight = 0
    while mstVertex>1:
        cheapest = [-1] * graph.size()
        for u,v,w in graph.edge:
            u_p = disjoint.find(u)
            v_p = disjoint.find(v)
            if u_p != v_p:
                if cheapest[u_p] == -1 or cheapest[u_p][2] > w:
                    cheapest[u_p] = (u, v, w)
                if cheapest[v_p] == -1 or cheapest[v_p][2] > w:
                    cheapest[v_p] = (u, v, w)
        for node in range(graph.size()):
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                u_p = disjoint.find(u)
                v_p = disjoint.find(v)
                if u_p != v_p:
                    disjoint.union(u_p, v_p)
                    print(u, '-->', v, '=', w)
                    mstVertex -= 1
                    weight += w
    print("total weight", weight)


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
boruvka_mst(graph)
