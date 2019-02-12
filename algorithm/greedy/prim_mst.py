import sys

"""
1)Create an empty set mstSet that keeps track of vertices included in mst
2)Assign a key value to all vertices in the input graph, initialize all key values as INFINITE, Assign key
value as 0 for the first vertex so that it is picked first
3)While mstSet not include all vertices
 a)Pick a vertex u not in mstSet and have minimum key value
 b)Include u to mstSet
 c)Update key value of all adjacent vertices of u. To update key values, iterate through all adjacent vertices
 . For every adjacent vertices v, if weight of edge u-v is less than the previous key value of v, update 
 the key value as weight of u-v
"""


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def prim_mst(self):
        # Array that store the mst
        mst = [False] * self.v
        # array for pich the minimum vertex that not in mst
        key = [sys.maxsize] * self.v
        # store mst edges
        parent = [-1] * self.v
        key[0] = 0  # pich the first vertex
        for i in range(self.v):
            u = Graph.min_vertices(key, mst)
            mst[u] = True
            for v in range(self.v):
                if not mst[v] and self.graph[u][v] != 0 and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.print_mst(parent)

    def print_mst(self, parent):
        for i in range(1, len(parent)):
            print(parent[i], '--', i, self.graph[parent[i]][i])

    @staticmethod
    def min_vertices(key, mst):
        """ find the minimum vertices that not in the mst """
        min_v = sys.maxsize
        for i in range(len(key)):
            if key[i] < min_v and not mst[i]:
                min_v = key[i]
                min_idx = i
        return min_idx


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.prim_mst()
