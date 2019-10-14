"""
Biconnected Component.
"""
from algorithm.graph.graph import UndirectedGraph

time = 0
count = 0


def bcc(graph):
    parent = [-1] * graph.size()
    st = []
    disc = [-1] * graph.size()
    low = [-1] * graph.size()

    for u in range(graph.size()):
        if parent[u] == -1:
            bc_util(graph, u, disc, low, st, parent)
        while len(st) > 0:
            w = st.pop()
            print(w[0], '-->', w[1], end='  ')
    global count
    print(count)


def bc_util(graph, u, disc, low, st, parent):
    global time, count
    time += 1
    disc[u] = low[u] = time
    for v in graph.graph[u]:
        if disc[v] == -1:
            st.append((u, v))
            parent[v] = u
            bc_util(graph, v, disc, low, st, parent)
            low[u] = min(low[u], low[v])

            if low[v] >= disc[u]:
                count += 1
                w = -1
                while w != (u, v):
                    w = st.pop()
                    print(w[0], '-->', w[1], end='  ')
                print()
        elif v != parent[u] and low[u] > disc[v]:
            low[u] = min(low[u], disc[v])
            st.append((u, v))


graph = UndirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(1, 5)
graph.add_edge(0, 6)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(7, 8)
graph.add_edge(8, 9)
graph.add_edge(10, 11)

bcc(graph)