# Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all
# the vertices together. A minimum spanning tree for a weighted, connected, undirected graph is a spanning tree with
# weight is smaller than or equal to the weight of every other spanning tree


class Graph:
    def __init__(self, v):
        self.graph = []
        self.v = v

    def add_edge(self, v, u, w):
        self.graph.append([v, u, w])


class DisjointSet:
    def __init__(self, v):
        self.parent = list(range(v))
        self.rank = [0] * v

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = i
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = j
        else:
            self.parent[x] = j
            self.rank[j] += 1


def kruskal_mst(g):
    disjointset = DisjointSet(g.v)
    g.graph.sort(key=lambda x:x[2])
    i = e = 0
    res = []
    while e < g.v-1:
        u, v, w = g.graph[i]
        uroot = disjointset.find(u)
        vroot = disjointset.find(v)
        if uroot != vroot:
            e += 1
            disjointset.union(uroot, vroot)
            res.append(g.graph[i])
        i += 1
    return res


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.add_edge(1, 2, 8)
    print(kruskal_mst(g))
