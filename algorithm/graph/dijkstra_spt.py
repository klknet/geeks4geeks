"""
Dijkstra's shortest path algorithm.
"""
import sys
import heapq
from algorithm.graph.graph import UndirectedWeightGraph

INF = sys.maxsize


def dijkstra(graph, s):
    spt = [False] * graph.size()
    dist = [INF] * graph.size()
    dist[s] = 0
    parent = [-1] * graph.size()
    c = graph.size()
    while c > 0:
        u = findMin(dist, spt)
        spt[u] = True
        for v, w in graph.graph[u]:
            if not spt[v] and dist[u] != INF and dist[v] > w + dist[u]:
                dist[v] = w + dist[u]
                parent[v] = u
        c -= 1
    # print_spt(dist, s)
    print("shortest path is")
    print_path(dist, parent, s)


def print_path(dist, parent, s):
    for v in range(len(dist)):
        if v != s:
            path_util(parent, v)
            print('=', dist[v])
        else:
            print(s, '-->', s, '=', 0)


def path_util(parent, v):
    if parent[v] != -1:
        print(v, '-->', parent[v], end="  ")
        path_util(parent, parent[v])



def findMin(dist, spt):
    min_v = INF
    m = 0
    for v in range(len(dist)):
        if not spt[v] and dist[v] < min_v:
            min_v = dist[v]
            m = v
    return m


def print_spt(dist, s):
    for u in range(len(dist)):
        if u != s:
            print(s, '-->', u, dist[u])


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
dijkstra(graph, 0)
