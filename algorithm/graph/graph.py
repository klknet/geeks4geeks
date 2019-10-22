from collections import defaultdict


class DirectedGraph(object):
    def __init__(self):
        self.edge = defaultdict(list)
        self.graph = defaultdict(list)
        self.vertex = set()

    def add_edge(self, u, v):
        self.edge[u].append(v)
        self.graph[u].append(v)
        self.vertex.add(u)
        self.vertex.add(v)

    def size(self):
        return len(self.vertex)


class UndirectedGraph(object):
    def __init__(self):
        self.edge = []
        self.graph = defaultdict(list)
        self.vertex = set()

    def add_edge(self, u, v):
        self.edge.append((u, v))
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.vertex.add(u)
        self.vertex.add(v)

    def size(self):
        return len(self.vertex)


class UndirectedWeightGraph(object):
    def __init__(self):
        self.edge = []
        self.graph = defaultdict(list)
        self.vertex = set()

    def add_edge(self, u, v, w):
        self.edge.append((u, v, w))
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        self.vertex.add(u)
        self.vertex.add(v)

    def size(self):
        return len(self.vertex)


class DirectedWeightGraph(object):
    def __init__(self):
        self.edge = []
        self.graph = defaultdict(list)
        self.vertex = set()

    def add_edge(self, u, v, w):
        self.vertex.add(u)
        self.vertex.add(v)
        self.edge.append((u, v, w))
        self.graph[u].append((v, w))

    def size(self):
        return len(self.vertex)


class DirectedWeightMatrixGraph(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def size(self):
        return len(self.matrix[0])


class DisjointSet(object):
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, u):
        if self.parent[u] != -1:
            return self.find(self.parent[u])
        return u

    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)
        self.parent[p_u] = p_v

