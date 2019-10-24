"""
Shortest Path Tree in Directed Acyclic Graph.
"""
import sys
from algorithm.graph.graph import DirectedWeightGraph


INF = sys.maxsize

def dag_spt(graph, s):
    visited = [False] * graph.size()
    dist = [INF] * graph.size()
    dist[s] = 0
    Stack = []
    for v in range(graph.size()):
        if not visited[v]:
            topological_util(graph, visited, v, Stack)
    while len(Stack) > 0:
        u = Stack.pop()
        if dist[u] != INF:
            for v, w in graph.graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
    print_spt(dist, s)


def topological_util(graph,visited, u, Stack):
    visited[u] = True
    for v,w in graph.graph[u]:
        if not visited[v]:
            topological_util(graph, visited, v, Stack)
    Stack.append(u)


def print_spt(dist, s):
    for u in range(len(dist)):
        if u != s:
            print(s, '-->', u, 'INF' if dist[u]==INF else dist[u])


graph = DirectedWeightGraph()
graph.add_edge(0,1,5)
graph.add_edge(0,2,3)
graph.add_edge(1,3,6)
graph.add_edge(1,2,2)
graph.add_edge(2,4,4)
graph.add_edge(2,5,2)
graph.add_edge(2,3,7)
graph.add_edge(3,4,-1)
graph.add_edge(4,5,-2)
dag_spt(graph, 1)