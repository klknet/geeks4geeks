"""
Convex hull graham scan.
1)Find the bottom-most point by comparing y coordinate of all points. If there are two points with same y value, then the
point with smaller x coordinate value will be considered. Let the bottom-most point be p0. Put p0 at first position in
output hull.
2)Consider the remaining n-1 points and sort them by polar angle in counterclockwise order around p0. If the polar angle
of two points is the same, then put the nearest point first.
3)After sorting, check if two or more points have same angle. If two more points have the same angle, then remove all same
angle points except the point farthest from p0. Let the size of new array be m.
4)If m is less than 3, return(Convex hull not possible)
5)Create an empty stack s and push points[0], points[1] and points[2] to s.
6)Process the remaining m-3 points one by one. Do following for every 'points[i]'
    1)Keeping removing points from stack while orientation of following three points is not counterclockwise..
        a)Point next to top of the stack.
        b)Point at the top of the stack.
        c)points[i].
    2)Push points[i] to stack.
7)Print contents of s.
"""
from algorithm.geometric.segments_intersect import Point
from functools import cmp_to_key
import copy

p0 = None


def convex_hull(points):
    global p0
    n = len(points)
    m = 0
    # find the left most point
    for i in range(1, n):
        if points[i].y < points[m].y or (points[i].y == points[m].y and points[i].x < points[m].x):
            m = i
    p0 = points[m]
    points[0], points[m] = points[m], points[0]
    s = []
    m = 0
    ns = copy.deepcopy(points[1:])
    # sort by polar angle
    ns.sort(key=cmp_to_key(polar_angle_cmp))
    ns.insert(0, p0)
    points = ns
    i = 1
    while i < n:
        while i < n - 1 and orientation(p0, points[i], points[i + 1]) == 0:
            i += 1
        m += 1
        points[m] = points[i]
        i += 1
    # less than 3 points cannot build a convex
    if m < 3:
        return
    s.append(p0)
    s.append(points[1])
    s.append(points[2])
    for i in range(3, m+1):
        while orientation(s[-2], s[-1], points[i]) != 2:
            s.pop()
        s.append(points[i])
    return s


def polar_angle_cmp(p1, p2):
    global p0
    delta = orientation(p0, p1, p2)
    if delta == 0:
        return 1 if distance(p0, p1) > distance(p0, p2) else -1
    return 1 if delta == 1 else -1


def distance(p1, p2):
    return (p1.x - p2.x)**2 + (p2.y - p2.y)**2


def orientation(p0, p1, p2):
    delta = (p1.x - p0.x) * (p2.y - p0.y) - (p1.y - p0.y) * (p2.x - p0.y)
    if delta == 0:
        return 0
    return 2 if delta > 0 else 1


points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
ch = convex_hull(points)
for p in ch:
    print(p)
