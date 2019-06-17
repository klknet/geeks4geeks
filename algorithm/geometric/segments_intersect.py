"""
How to check if two given segments intersect.
Orientation of an ordered triplet of points in the plane can be
- counterclockwise
- clockwise
- colinear

Two segments (p1, q1) and (p2, q2) intersect if and only if one of the following conditions is verified.
1.General Case.
-- (p1, q1, p2) and (p1, q1, q2) have different orientation and
-- (p2, q2, p1) and (p2, q2, q1) have different orientation.
2.Special Case.
-- (p1, q1, p2) (p1, q1, q2) (p2, q2, p1) and (p2, q2, q1) are all colinear and.
-- the x-projection of (p1, q1) and (p2, q2) intersect.
-- the y-projection of (p1, q1) and (p2, q2) intersect.
"""


def intersect(seg1, seg2):
    o1 = orientation(seg1.p, seg1.q, seg2.p)
    o2 = orientation(seg1.p, seg1.q, seg2.q)
    o3 = orientation(seg2.p, seg2.q, seg1.p)
    o4 = orientation(seg2.p, seg2.q, seg1.q)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and onsegment(seg1.p, seg1.q, seg2.p):
        return True
    if o2 == 0 and onsegment(seg1.p, seg1.q, seg2.q):
        return True
    if o3 == 0 and onsegment(seg2.p, seg2.q, seg1.p):
        return True
    if o4 == 0 and onsegment(seg2.p, seg2.q, seg1.q):
        return True
    return False


def onsegment(p1, p2, p3):
    return min(p1.x, p2.x) < p3.x < max(p1.x, p2.x) and min(p1.y, p2.y) < p3.y < max(p1.y, p2.y)


def orientation(p1, p2, p3):
    """
    :param p1:
    :param p2:
    :param p3:
    :return: 0 - co-linear   1 - counterclockwise  2 -- clockwise
    """
    detb = (p1.x - p2.x) * (p3.y - p2.y) - (p3.x - p2.x) * (p1.y - p2.y)
    if detb == 0:
        return detb
    if detb > 0:
        return 2
    return 1


class Segment(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


seg1 = Segment(Point(1, 1), Point(10, 1))
seg2 = Segment(Point(1, 2), Point(10, 2))
print(intersect(seg1, seg2))

seg1 = Segment(Point(10, 0), Point(0, 10))
seg2 = Segment(Point(0, 0), Point(10, 10))
print(intersect(seg1, seg2))

seg1 = Segment(Point(-5, -5), Point(0, 0))
seg2 = Segment(Point(1, 1), Point(10, 10))
print(intersect(seg1, seg2))
