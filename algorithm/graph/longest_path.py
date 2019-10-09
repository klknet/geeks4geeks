"""
Longest path in a Directed Acyclic Graph.
"""
import sys
from algorithm.graph.graph import DirectedWeightGraph

NINF = -sys.maxsize


def longest_path(graph, s):
    Stack = []
    visited = [False] * graph.size()
    dist = [NINF] * graph.size()
    dist[s] = 0
    for v in range(graph.size()):
        if not visited[v]:
            topologicalSort(graph, v, visited, Stack)
    while len(Stack) > 0:
        u = Stack.pop()
        if dist[u] != NINF:
            for v, w in graph.graph[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
    return dist


def topologicalSort(graph, u, visited, Stack):
    visited[u] = True
    adj = graph.graph[u]
    for v, w in adj:
        if not visited[v]:
            topologicalSort(graph, v, visited, Stack)
    Stack.append(u)


graph = DirectedWeightGraph()
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 6)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(2, 5, 2)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 5, 1)
graph.add_edge(3, 4, -1)
graph.add_edge(4, 5, 2)

print(longest_path(graph, 1))
