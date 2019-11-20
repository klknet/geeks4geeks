"""
Graph Coloring.
"""
from algorithm.graph.graph import UndirectedGraph


def graph_color(graph):
    available = [False] * graph.size()
    result = [-1] * graph.size()
    cr = 0
    result[0] = 0
    for u in range(1, graph.size()):
        # color all adjacent vertices.
        for v in graph.graph[u]:
            if result[v] != -1:
                available[result[v]] = True
        for i in range(len(available)):
            if not available[i]:
                cr = i
                break
        result[u] = cr
        for v in graph.graph[u]:
            if result[v] != -1:
                available[result[v]] = False
    for u in range(graph.size()):
        print('vertex', u, 'color', result[u])


g1 = UndirectedGraph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
graph_color(g1)

print()

g2 = UndirectedGraph()
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(1, 2)
g2.add_edge(1, 4)
g2.add_edge(2, 4)
g2.add_edge(4, 3)
graph_color(g2)