import sys
from collections import defaultdict
from heapq import heappush, heappop


class Node:
    def __init__(self, v, d):
        self.v = v
        self.d = d

    def __eq__(self, other):
        return self.d == other.d

    def __lt__(self, other):
        return self.d < other.d


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v, dist):
        self.graph[u].insert(0, [v, dist])
        self.graph[v].insert(0, [u, dist])

    def prim_mst(self):
        mst = [False] * self.v
        parent = [-1] * self.v
        key = [sys.maxsize] * self.v
        key[0] = 0
        heap = [Node(0, 0)]

        while len(heap) > 0:
            node = heappop(heap)
            if mst[node.v]:
                continue
            mst[node.v] = True
            for v in self.graph[node.v]:
                if not mst[v[0]] and v[1] < key[v[0]]:
                    key[v[0]] = v[1]
                    heappush(heap, Node(v[0], v[1]))
                    parent[v[0]] = node.v

        self.print_mst(parent)

    def print_mst(self, parent):
        for i in range(1, len(parent)):
            print(parent[i], '--', i)


graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 8, 2)
graph.add_edge(2, 5, 4)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(6, 8, 6)
graph.add_edge(7, 8, 7)
graph.prim_mst()
