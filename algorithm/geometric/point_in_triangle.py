"""
Check whether a given point lies in a triangle or not.
Given three corner points of a triangle, and one more point P. Write a function to check whether P lies within the triangle
or not.
"""

from algorithm.geometric.segments_intersect import Point


def in_triangle(A, B, C, P):
    area_ABC = abs(((B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y)) / 2)
    area_ABP = abs(((B.x - A.x) * (P.y - A.y) - (P.x - A.x) * (B.y - A.y)) / 2)
    area_ACP = abs(((C.x - A.x) * (P.y - A.y) - (P.x - A.x) * (C.y - A.y)) / 2)
    area_PBC = abs(((B.x - P.x) * (C.y - P.y) - (C.x - P.x) * (B.y - P.y)) / 2)
    if area_ABC == area_ABP + area_ACP + area_PBC:
        return True
    return False


A = Point(0, 0)
B = Point(20, 0)
C = Point(10, 30)
P = Point(10, 15)
print(in_triangle(A, B, C, P))
