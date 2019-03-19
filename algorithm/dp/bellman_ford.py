"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.
Bellman-Ford Algorithm.
1)This step initializes distances from source to all vertices as infinite and distance to source itself as 0. Create an
array dist[] of size |v| with all values of infinite except dist[src] where src is source vertex.
2)This step calculates shortest distances. Do following |v|-1 times where v is the number of vertices in given graph.
..a)Do following for each edge u-v:
.......If dist[v] > dist[u]+w(u,v)  then dist[v] = dist[u]+dist[v]
3)This step reports if there is a negative cycle in graph. Do following for each edge u-v.
..If dist[v]>dist[u]+w(u,v) then 'Graph contains negative weight cycle'.
"""

import sys


def bellman_ford(g, src):
    # step 1, initialize distances from source to all vertices.
    dist = [sys.maxsize] * g.v
    dist[src] = 0
    # step 2, relax all edges for v-1 times
    for k in range(g.v):
        for u, v, w in g.graph:
            if dist[u] != sys.maxsize and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    # step 3, check for if negative cycle exists.
    for u, v, w in g.graph:
        if dist[u] != sys.maxsize and dist[v] > dist[u] + w:
            return False
    print_arr(dist, src)
    return True


def print_arr(dist, src):
    print('Vertex   Distance from source')
    for i in range(len(dist)):
        if i != src:
            print('%d \t\t %d' %(i, dist[i]))


class Graph(object):
    def __init__(self, Vertices):
        self.v = Vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

g = Graph(5)
g.add_edge(0, 1, -1) 
g.add_edge(0, 2, 4) 
g.add_edge(1, 2, 3) 
g.add_edge(1, 3, 2) 
g.add_edge(1, 4, 2) 
g.add_edge(3, 2, 5) 
g.add_edge(3, 1, 1) 
g.add_edge(4, 3, -3)
bellman_ford(g, 0)
