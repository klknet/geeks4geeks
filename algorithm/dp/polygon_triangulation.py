"""
A triangulation of a convex polygon is formed by drawing diagonals between non-adjacent vertices such that the diagonals
never intersects.
The idea is to divide the polygon into three parts: a single triangle, the sub-polygon to the left, and the sub-polygon
to the right. We try all possible divisions like this and find the one that minimises the cost of the triangle plus the
cost of the triangulation of the two sub-polygons.
Let Minimum Cost Of Triangulation of vertices from i to j be minCost(i,j)
If j<i+2, then
    minCost(i,j)=0
Else
    minCost(i,j) = Min{ minCost(i,k) + minCost(k,j) +cost(i,j,k) } Here k varies from  i+1 to j-1

Cost of a triangle formed by edgess (i,j), (j,k) and (k,i) is
    cost(i,j,k) = dist(i,j)+dist(j,k)+dist(k,i)
"""

import math
import sys


def min_cost_dp(point: list):
    n = len(point)
    t = [[0 for col in range(n)] for row in range(n)]
    for gap in range(2, n):
        for i in range(n-gap):
            j = i+gap
            m_cost = sys.maxsize
            for k in range(i+1, j):
                cost = t[i][k]+t[k][j]+weight(point[i], point[j], point[k])
                m_cost = min(m_cost, cost)
            t[i][j] = m_cost
    return t[0][n-1]


def min_cost(point: list, i, j):
    if j < i + 2:
        return 0
    m_cost = sys.maxsize
    for k in range(i+1, j):
        cost = min_cost(point, i, k)+min_cost(point, k, j)+weight(point[i], point[j], point[k])
        m_cost = min(m_cost, cost)
    return m_cost


def weight(i, j, k):
    return i.distance(j)+j.distance(k)+i.distance(k)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


points = [Point(0,0), Point(1,0), Point(2,1), Point(1,2), Point(0,2)]
print(min_cost(points, 0, len(points)-1))
print(min_cost_dp(points))
