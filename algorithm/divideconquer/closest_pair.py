"""
Closest pair of points.
As a pre-processing step, input array is sorted according x coordinates.
1)Find the middle point in the sorted array, we can take P[n/2] as middle point.
2)Divide the given array in two halves. The first subarray contains points from P[0] to P[n/2]. The second subarray
contains points from P[n/2+1] to P[n-1].
3)Recursively find the smallest distances in both subarrays. Let the distances be dl and dr. Find the minimum of dl and
dr. Let the minimum be d.
4)From above 3 steps, we have an upper bound d of minimum distance. Now we need to consider the pairs such that one point
in pair is from left half half and the other is from right half. Consider the vertical line passing through P[n/2] and
find all points whose x coordinates is closer than d to the middle vertical line. Build an array strip[] of all such pints.
5)Sort the array strip[] according to y coordinates.
6)Find the smallest distance in strip[].
7)Finally return the minimum of d and distance calculated in above step.
"""

import sys
import copy
import math


def closest_pair(arr, l, r):
    if l+1 == r:
        return distance(arr[l], arr[r])
    m = (l + r) >> 1
    dl = closest_pair(arr, l, m)
    dr = closest_pair(arr, m + 1, r)
    d = min(dl, dr)
    for i in range(l, m + 1):
        if arr[m].x - arr[i].x < d:
            break
    for j in range(r, m, -1):
        if arr[j].x - arr[m].x < d:
            break
    dm = strip(copy.deepcopy(arr[i:j + 1]), d)
    return min(d, dm)


def strip(arr, d):
    arr.sort(key=lambda p: p.y)
    n = len(arr)
    for i in range(0, n):
        j = i + 1
        while j < n and arr[j].y - arr[i].y < d:
            d_ij = distance(arr[i], arr[j])
            if d_ij<d:
                d = d_ij
            j += 1
    return d


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4),  Point(24, 28), Point(6, 3)]
points.sort(key = lambda p: p.x)
print(closest_pair(points, 0, len(points) -1))
