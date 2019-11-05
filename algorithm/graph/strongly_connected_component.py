"""
Strongly connected component.
Following is Kosaraju's Algorithm.
1)Create a empty stack and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices
of a vertex, push the vertex to stack.
2)Reverse directions of all arcs to obtain the transpose graph.
3)One by one pop a vertex from S while S is not empty. Let the popped vertex be V. Take V as source and do DFS. The DFS
starting from V prints strongly connected components of v.
"""
from algorithm.graph.graph import DirectedGraph


def scc(graph):
    Stack = []
    visited = [False] * graph.size()
    for u in range(graph.size()):
        if not visited[u]:
            fill_order(graph, u, visited, Stack)
    transpose = get_transpose(graph)
    for i in range(len(visited)):
        visited[i] = False
    while len(Stack)>0:
        u = Stack.pop()
        if not visited[u]:
            dfs_util(transpose, u, visited)
            print()


def dfs_util(graph, u, visited):
    visited[u] = True
    print(u, end=' ')
    for v in graph.graph[u]:
        if not visited[v]:
            dfs_util(graph, v, visited)


def get_transpose(graph):
    t = DirectedGraph()
    for u in range(graph.size()):
        for v in graph.graph[u]:
            t.add_edge(v, u)
    return t


def fill_order(graph, u, visited, Stack):
    visited[u] = True
    for v in graph.graph[u]:
        if not visited[v]:
            fill_order(graph, v, visited, Stack)
    Stack.append(u)


g1 = DirectedGraph()
g1.add_edge(1,0)
g1.add_edge(0,2)
g1.add_edge(2,1)
g1.add_edge(0,3)
g1.add_edge(3,4)
scc(g1)