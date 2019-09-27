"""
Breadth first search or a BFS for a graph.
"""
from collections import defaultdict
from algorithm.graph.graph import DirectedGraph


def bfs(graph, start):
    visited = [0] * graph.size()
    queue = [start]
    visited[start] = 1
    while len(queue) > 0:
        v = queue.pop()
        print(v, end=' ')
        edges = graph.edge[v]
        for e in edges:
            if not visited[e]:
                queue.insert(0, e)
                visited[e] = 1


graph = DirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
bfs(graph, 2)
