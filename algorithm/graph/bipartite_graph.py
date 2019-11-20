"""
Check whether a graph is bipartite or not.
"""
from algorithm.graph.graph import UndirectedGraph


def bipartite(graph, src):
    visited = [False] * graph.size()
    color = [-1] * graph.size()
    color[src] = 1
    queue = []
    queue.insert(0, src)
    while len(queue) > 0:
        u = queue.pop()
        visited[u] = True
        for v in graph.graph[u]:
            if not visited[v]:
                queue.insert(0, v)
                color[v] = 1 ^ color[u]
            else:
                if color[u] == color[v]:
                    return False
    return True



graph = UndirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(4, 3)
graph.add_edge(4, 5)
graph.add_edge(0, 5)
# graph.add_edge(0, 2)

print(bipartite(graph, 0))


queue = []
queue.append(1)
queue.append(2)
queue.append(3)
while len(queue)>0:
    print(queue.pop())
