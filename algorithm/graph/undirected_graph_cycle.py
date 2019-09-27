"""
Disjoint Set. Detect Cycle in an Undirected graph.
"""
from algorithm.graph.graph import UndirectedGraph, DisjointSet


def detect_cycle(graph, disjoint):
    for edge in graph.edge:
        u_p = disjoint.find(edge[0])
        v_p = disjoint.find(edge[1])
        if u_p != v_p:
            disjoint.union(edge[0], edge[1])
        else:
            print("have cycle", edge)
            return True
    return False


graph = UndirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(0, 2)
disjoint = DisjointSet(graph.size())
print(detect_cycle(graph, disjoint))