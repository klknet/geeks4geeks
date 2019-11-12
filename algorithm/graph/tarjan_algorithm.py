"""
Tarjan's Algorithm to find strongly connected components.
"""
from algorithm.graph.graph import DirectedGraph

time = 0


def scc(graph):
    stack_member = [False] * graph.size()
    low = [-1] * graph.size()
    Stack = []
    disc = [-1] * graph.size()
    for u in range(graph.size()):
        if disc[u] == -1:
            dfs_util(graph, u, stack_member, low, disc, Stack)


def dfs_util(graph, u, stack_member, low, disc, Stack):
    global time
    stack_member[u] = True
    low[u] = time
    disc[u] = time
    time += 1
    Stack.append(u)
    for v in graph.graph[u]:
        if disc[v] == -1:
            dfs_util(graph, v, stack_member, low, disc, Stack)
            low[u] = min(low[u], low[v])
        elif stack_member[v]:
            if low[u] > disc[v]:
                low[u] = disc[v]
    if low[u] == disc[u]:
        while len(Stack) > 0:
            c = Stack.pop()
            stack_member[c] = False
            print(c, end=' ')
            if c == u:
                break
        print()


print('scc in g1')
g1 = DirectedGraph()
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
scc(g1)
print('scc in g2')
g2 = DirectedGraph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
scc(g2)
print('scc in g3')
g3 = DirectedGraph()
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)
scc(g3)
print('scc in g4')
g4 = DirectedGraph()
g4.add_edge(0, 1)
g4.add_edge(0, 3)
g4.add_edge(1, 2)
g4.add_edge(1, 4)
g4.add_edge(2, 0)
g4.add_edge(2, 6)
g4.add_edge(3, 2)
g4.add_edge(4, 5)
g4.add_edge(4, 6)
g4.add_edge(5, 6)
g4.add_edge(5, 7)
g4.add_edge(5, 8)
g4.add_edge(5, 9)
g4.add_edge(6, 4)
g4.add_edge(7, 9)
g4.add_edge(8, 9)
g4.add_edge(9, 8)
scc(g4)
print('scc in g5')
g5 = DirectedGraph()
g5.add_edge(0, 1)
g5.add_edge(1, 2)
g5.add_edge(2, 3)
g5.add_edge(2, 4)
g5.add_edge(3, 0)
g5.add_edge(4, 2)
scc(g5)
