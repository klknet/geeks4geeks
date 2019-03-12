"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element.
Write a function to return the minimum number of jumps to reach the end of the array(starting from the first element).
If an element is zero, then cannot move through that element.
A native approach is to start from the first element and recursively call for all the elements reachable from the first
element. The minimum number of jumps to reach end from first can be calculated using minimum number of jumps needed to
reach end from the elements reachable from first.
minJumps(start, end) = min(min(k, end)) for all k reachable from first.
"""

import sys


def min_jumps(arr, s, e):
    # base case: when source and destination are same.
    if e == s + 1:
        return 0
    # when nothing is reachable from the given source.
    if arr[s] == 0:
        return sys.maxsize
    jumps = sys.maxsize
    for k in range(s + 1, min(e, arr[s] + s + 1)):
        j = min_jumps(arr, k, e)
        if j != sys.maxsize and j + 1 < jumps:
            jumps = j + 1
    return jumps


def min_jumps_dp(arr):
    n = len(arr)
    t = [0] * n
    for i in range(n - 2, -1, -1):
        if arr[i] == 0:
            t[i] = sys.maxsize
        else:
            jumps = sys.maxsize
            for k in range(i+1, min(n, arr[i] + i + 1)):
                if t[k] != sys.maxsize and t[k] + 1 < jumps:
                    jumps = t[k] + 1
            t[i] = jumps
    return t[0]


arr = [1, 3, 6, 3, 2, 3, 6, 3, 9, 5]
# arr = [1]
print("Minimum number of jumps to reach end is", min_jumps(arr, 0, len(arr)))
print(min_jumps_dp(arr))
