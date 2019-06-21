"""
Convex Hull.
1)Initialize p as leftmost point.
2)Do following while we don't come back to the first point.
 a)The next point q is the point such that the triplet (p,q,r) is counterclockwise for any other point r.
 b)next[p]=q(store q as next of p in the output convex hull).
 c)p=q (set p as q for next iteration).
"""
from algorithm.geometric.segments_intersect import Point


def convex_hull(points):
    n = len(points)
    l = 0
    for i in range(1, n):
        if points[l].x > points[i].x:
            l = i
    ch = []
    p = l
    while True:
        ch.append(points[p])
        q = (p+1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return ch


def orientation(p1, p2, p3):
    """
    :param p1:
    :param p2:
    :param p3:
    :return: 0 colinear  1 clockwise  2 counterclockwise
    """
    delta = (p1.x-p2.x)*(p3.y-p2.y) - (p1.y-p2.y)*(p3.x-p2.x)
    if delta == 0:
        return 0
    return 1 if delta>0 else 2


points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), Point(3, 0), Point(0, 0), Point(3, 3)]
ch = convex_hull(points)
for p in ch:
    print(p)
