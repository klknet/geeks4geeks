"""
Vertex Cover problem.
"""
from algorithm.graph.graph import UndirectedGraph


def vertex_cover(graph):
    visited = [False] * graph.size()
    for u in range(graph.size()):
        if not visited[u]:
            for v in graph.graph[u]:
                if not visited[v]:
                    visited[u] = True
                    visited[v] = True
                    break
    for i in range(graph.size()):
        if visited[i]:
            print(i, end='  ')


g = UndirectedGraph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

vertex_cover(g)

g = UndirectedGraph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
vertex_cover(g)

