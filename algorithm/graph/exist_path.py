"""
Find if there is a path between two vertices in a directed graph.
"""
from algorithm.graph.graph import DirectedGraph


def exist_path(graph, s, d):
    Stack = []
    res = dfs_util(graph, [False]*graph.size(), s, d, Stack)
    print(Stack)
    return res


def dfs_util(graph, visited, u, d, Stack):
    visited[u] = True
    Stack.append(u)
    for v in graph.graph[u]:
        if v == d:
            return True
        if not visited[v]:
            if dfs_util(graph, visited, v, d, Stack):
                return True
    Stack.pop()
    return False


graph = DirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print(exist_path(graph, 1, 3))
print(exist_path(graph, 3, 1))
