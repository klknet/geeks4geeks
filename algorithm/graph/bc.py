"""
Biconnected components.
"""
from algorithm.graph.graph import UndirectedGraph

time = 0


def bc(graph):
    visited = [False] * graph.size()
    low = [-1] * graph.size()
    parent = [-1] * graph.size()
    disc = [-1] * graph.size()
    Stack = []
    for u in range(graph.size()):
        if not visited[u]:
            dfs_util(graph, u, visited, low, parent, disc, Stack)
            while len(Stack) > 0:
                c = Stack.pop()
                print(c[0], '-->', c[1], end='   ')
            print()



def dfs_util(graph, u, visited, low, parent, disc, Stack):
    global time
    visited[u] = True
    children = 0
    disc[u] = time
    low[u] = time
    time += 1
    for v in graph.graph[u]:
        if not visited[v]:
            Stack.append((u, v))
            children += 1
            parent[v] = u
            dfs_util(graph, v, visited, low, parent, disc, Stack)
            low[u] = min(low[u], low[v])
            if (parent[u] != -1 and low[v] >= disc[u]) or (parent[u] == -1 and children > 1):
                while len(Stack) > 0:
                    c = Stack.pop()
                    print(c[0], '-->', c[1], end='  ')
                    if c[0] == u:
                        break
                print()
        elif v != parent[u]:
            if low[u] > disc[v]:
                Stack.append((u, v))
                low[u] = disc[v]


g = UndirectedGraph()
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 1)
g.add_edge(1, 3)
g.add_edge(3, 1)
g.add_edge(2, 3)
g.add_edge(3, 2)
g.add_edge(2, 4)
g.add_edge(4, 2)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(1, 5)
g.add_edge(5, 1)
g.add_edge(0, 6)
g.add_edge(6, 0)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(5, 7)
g.add_edge(7, 5)
g.add_edge(5, 8)
g.add_edge(8, 5)
g.add_edge(7, 8)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(9, 8)
g.add_edge(10, 11)
g.add_edge(11, 10)

bc(g)