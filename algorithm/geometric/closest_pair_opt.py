"""
Closet Pair of Points | O(nlog^n)
"""

import sys
import math
import copy


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def closest_pair_util(px, py, n):
    if n <= 3:
        return brute_force(px, n)
    m = n >> 1
    pl = [None]*m
    pr = [None]*(n-m)
    li = ri = 0
    # partition points around middle point according y coordinate.
    for i in range(n):
        if py[i].x < px[m].x:
            pl[li] = py[i]
            li += 1
        else:
            pr[ri] = py[i]
            ri += 1
    dl = closest_pair_util(px, pl, m)
    dr = closest_pair_util(px[m:], pr, n - m)
    d = min(dl, dr)
    strip = [None] * n
    j = 0
    for i in range(n):
        if abs(py[i].x - px[m].x) < d:
            strip[j] = py[i]
            j += 1
    return min(d, strip_distance(strip, j, d))


def strip_distance(strip, n, d):
    for i in range(n):
        j = i + 1
        while j < n and strip[j].y - strip[i].y < d:
            d = min(d, distance(strip[i], strip[j]))
            j += 1
    return d


def brute_force(px, n):
    m = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            m = min(m, distance(px[i], px[j]))
    return m


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4), Point(24, 28), Point(6, 3)]
px = copy.copy(points)
py = copy.copy(points)
px.sort(key=lambda p: p.x)
py.sort(key=lambda p: p.y)

print(closest_pair_util(px, py, len(px)))
