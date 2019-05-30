"""
M coloring problem.
Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two
adjacent vertices of the graph are colored with the same color. Here coloring of a graph means assignment of colors to
all vertices.
"""


class Graph(object):
    def __init__(self, n, m):
        self.v = n
        self.matrix = m
        self.color = [0] * n

    def isSafe(self, v, c):
        for i in range(self.v):
            if self.matrix[i][v] == 1 and self.color[i] == c:
                return False
        return True

    def print_solution(self):
        print(self.color)


def m_color(graph, m):
    if not m_color_util(graph, 0, m):
        print('no solution')


def m_color_util(graph, v, m):
    if v == graph.v:
        print(graph.color)
        return True
    exists = True
    for i in range(1, m+1):
        if graph.isSafe(v, i):
            graph.color[v] = i
            exists = m_color_util(graph, v+1, m) or exists
            graph.color[v] = 0 # backtrack
    return exists


matrix = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
graph = Graph(4, matrix)
m_color(graph, 3)
