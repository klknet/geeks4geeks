"""
How to check if a given point lies inside or outside of a polygon.
1)Draw a horizontal line to the right of each point and extend it to infinity.
2)Count the number of times the line intersects with polygon edges.
3)A point is inside the polygon either count of intersections is odd or point lies on an edge of polygon. If none of the
condition is true, then point lies outside.
"""

from algorithm.geometric.segments_intersect import *


def in_polygon(polygon, point):
    n = len(polygon)
    i = count = 0
    inf = Point(99999999, point.y)
    while 1:
        next_i = (i + 1) % n
        if intersect(Segment(polygon[i], polygon[next_i]), Segment(point, inf)):
            # check if given point colinear with current line
            if orientation(polygon[i], polygon[next_i], point) == 0:
                return onsegment(polygon[i], polygon[next_i], point)
            count += 1
        i = next_i
        if i == 0:
            break
    return True if count & 1 else False


polygon = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
print(in_polygon(polygon, Point(20, 20)))
print(in_polygon(polygon, Point(5, 5)))

polygon = [Point(0, 0), Point(5, 5), Point(5, 0)]
print(in_polygon(polygon, Point(3, 3)))
print(in_polygon(polygon, Point(5, 1)))
print(in_polygon(polygon, Point(8, 1)))

polygon = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
print(in_polygon(polygon, Point(-1, 10)))
