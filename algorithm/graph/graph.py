from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.edge = defaultdict(list)

    def add_edge(self, u, v):
        self.edge[u].append(v)

    def size(self):
        return len(self.edge)
