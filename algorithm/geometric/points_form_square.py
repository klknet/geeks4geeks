"""
Given coordinates of four points in a plane, find if the four points form a square or not.
The idea is to pick any point and calculate its distance from rest of points. Let the picked point be 'p'. To form a square,
distance of two points must be same from 'p', let this distance be d. The distance from one point must be different from
that d and must be equal to square root of 2 times d. Let this point with different distance be q.
The above condition is not good enough as the point with different distance can be on the other hand. We also need check
that q is at same distance from 2 other points and this distance is same as d.
"""

from algorithm.geometric.segments_intersect import Point


def form_a_square(p1, p2, p3, p4):
    d_12 = distance(p1, p2)
    d_13 = distance(p1, p3)
    d_14 = distance(p1, p4)

    if d_12 == d_13:
        d = d_12
        if d_14 == d * 2 and distance(p4, p2) == d == distance(p4, p3):
            return True
    elif d_12 == d_14:
        d = d_12
        if d_13 == d * 2 and distance(p4, p2) == d == distance(p4, p3):
            return True
    elif d_13 == d_14:
        d = d_13
        if d_12 == d * 2 and distance(p4, p2) == d == distance(p2, p3):
            return True

    return False


def distance(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


p1, p2, p3, p4 = Point(20, 10), Point(10, 20), Point(20, 20), Point(10, 10)
print(form_a_square(p1, p2, p3, p4))
