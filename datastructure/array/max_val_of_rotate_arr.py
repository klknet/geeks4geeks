"""
Find maximum value of sum (i*arr[i]) with only rotations on given array allowed.
"""
import sys


def max_sum(arr):
    cur = 0
    s = 0
    res = -sys.maxsize
    for i in range(len(arr)):
        cur += i * arr[i]
        s += arr[i]
    for i in range(1, len(arr)):
        cur = cur + len(arr) * arr[i-1] - s
        if cur > res:
            res = cur
    return res


print(max_sum([1, 20, 2, 10]))
print(max_sum([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
