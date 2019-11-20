"""
Bellman-Ford Algorithm.
"""
from algorithm.graph.graph import DirectedWeightGraph
import sys

INF = sys.maxsize


def bellman_ford(graph, src):
    dist = [INF] * graph.size()
    dist[src] = 0
    for c in range(graph.size() -1):
        for u,v,w in graph.edge:
            if dist[u] != INF and dist[u]+w<dist[v]:
                dist[v] = dist[u] + w

    # check for negative weight cycle.
    for u,v,w in graph.edge:
        if dist[u] != INF and dist[u]+w<dist[v]:
            print("negative cycle found")
            return
    print_spt(dist, src)


def print_spt(dist, src):
    for v in range(len(dist)):
        if v != src:
            print(src, '-->', v, '=', dist[v] )
        else:
            print(src, '-->', src, '=', 0)


graph = DirectedWeightGraph()
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)
bellman_ford(graph, 0)