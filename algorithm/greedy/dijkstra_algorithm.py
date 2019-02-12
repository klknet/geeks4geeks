"""
Find the shortest path from a source vertex to all other vertices in a given graph
1)Create a spt(shortest path tree) set to keep track of vertices included in spt
2)Create a dist set to store distance from source vertex, initially value is INFINITE, set first value as 0 so that it
is picked first
3)While spt not contains all vertices, do
 a)get a minimum vertex u in dist and not in spt set
 b)put u to spt set
 c)update all adjacent vertex v of u, if distance of u and weight u-v is less than previous distance of v
4)Print the solution
"""

import sys


class Graph:
    def __init__(self, v):
        self.v = v
        # self.graph = [[0 for column in range(self.v)] for row in range(self.v)]
        # self.graph = matrix

    def dijkstra_spt(self, src):
        spt = [False] * self.v
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        for i in range(self.v):
            u = self.find_minimum(dist, spt)
            spt[u] = True
            for j in range(self.v):
                if not spt[j] and self.graph[u][j] != 0 and dist[j] > self.graph[u][j] + dist[u]:
                    dist[j] = dist[u] + self.graph[u][j]
        self.print_spt(dist)

    @staticmethod
    def print_spt(dist):
        print('Vertex', '\t', 'Distance from source')
        for i in range(len(dist)):
            print(i, '\t\t', dist[i])

    def find_minimum(self, dist, spt):
        min_v = sys.maxsize
        for i in range(self.v):
            if not spt[i] and dist[i] < min_v:
                min_v = dist[i]
                min_idx = i
        return min_idx


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra_spt(2)
