"""
Topological sorting.
"""

from algorithm.graph.graph import DirectedGraph


def topological_sort(graph):
    visited = [False] * graph.size()
    Stack = []
    for u in range(graph.size()):
        if not visited[u]:
            topological_util(graph, u, visited, Stack)
    return Stack


def topological_util(graph, u, visited, Stack):
    visited[u] = True
    adj = graph.graph[u]
    for v in adj:
        if not visited[v]:
            topological_util(graph, v, visited, Stack)
    Stack.append(u)


graph = DirectedGraph()
graph.add_edge(5, 2)
graph.add_edge(5, 0)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

stack = topological_sort(graph)
while len(stack) > 0:
    print(stack.pop(), end=' ')