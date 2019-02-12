from algorithm.structure.priority_queue import MinHeap
from collections import defaultdict
import sys


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].insert(0, Node(v, w))
        self.graph[v].insert(0, Node(u, w))

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        spt = [False] * self.v
        heap = MinHeap([Node(src, 0)])
        while not heap.empty():
            u = heap.pop()
            if spt[u.k]:
                continue
            spt[u.k] = True
            for vertex in self.graph[u.k]:
                if not spt[vertex.k] and dist[vertex.k] > dist[u.k] + vertex.v:
                    dist[vertex.k] = dist[u.k] + vertex.v
                    heap.push(Node(vertex.k, dist[vertex.k]))
        self.print_spt(dist)

    @staticmethod
    def print_spt(dist):
        print('vertex', '\tDistance from source')
        for i in range(len(dist)):
            print(i, '\t\t', dist[i])


class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v


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
graph.dijkstra(3)
