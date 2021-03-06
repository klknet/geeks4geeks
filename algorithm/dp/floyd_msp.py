"""
The problem is to find the shortest distances between every pair of vertices in a given edge weighted directed graph.
Floyd Warshall Algorithm.
We initialize the solution matrix same as the input matrix graph as a first step. Then we update the solution matrix by
considering all vertices as an intermediate vertex. The idea is to one by one pick all vertices and updates all shortest
paths which include the picked vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an
intermediate vertex, we already considered vertices {0,1,2,...k-1} as intermediate vertices. For every pair(i,j), of
source and destination vertices respectively, there are two possible cases:
1)k is not an intermediate vertex in shortest path from i to j, we keep the value of dist[i[[j] as it is.
2)k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k]+dist[k][j]
if dist[i][j]>dist[i][k]+dist[k][j].
"""
import sys
import copy

INF = sys.maxsize


def floyd_msp(graph):
    # init matrix dist same as graph, so distance of every pair vertices are not having any intermediate vertices.
    # dist = map(lambda i: map(lambda j: j, i), graph)
    dist = copy.deepcopy(graph)
    v = len(graph)
    # store the predecessor information.
    path = copy.deepcopy(graph)
    for i in range(v):
        for j in range(v):
            if i != j and graph[i][j] != INF:
                path[i][j] = i
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if i != j and dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k
    print_solution(dist)
    print_path(dist, path)


def print_solution(dist):
    v = len(dist)
    for i in range(v):
        for j in range(v):
            if dist[i][j] == INF:
                print("INF", end='\t')
            else:
                print(dist[i][j], end='\t')
        print()


# print the shortest path between every pair vertices of the weighted directed graph.
def print_path(dist, path):
    v = len(dist)
    for i in range(v):
        for j in range(v):
            if i != j and path[i][j] != INF:
                print("The shortest path from %d to %d is " % (i, j), end='')
                print(i, end='')
                p = path[i][j]
                while p != i:
                    print("-->", p, end='')
                    p = path[i][p]
                print("-->", j, '\t', end='')
                print(dist[i][j])


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
floyd_msp(graph)
