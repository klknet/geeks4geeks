"""
Find next greater number with same set of digits.
"""
import sys


def floor_number(arr):
    n = len(arr)
    i = j = -1
    for k in range(n - 1, 0, -1):
        if arr[k] > arr[k - 1]:
            i = k - 1
    if i == -1:
        return None
    l, h = i + 1, n - 1
    while l < h:
        m = ((l + h) >> 1) + 1
        if arr[m] < arr[i]:
            h = m - 1
        else:
            l = m
    j = l
    arr[i], arr[j] = arr[j], arr[i]
    remain = list(reversed(arr[i + 1:]))
    return arr[:i + 1] + remain


print(floor_number([5, 3, 4, 9, 7, 6]))
