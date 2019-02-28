"""
Given an array of positive integers. Write a program to find the sum of the maximum sum subsequence of the given array
such that the integers in the subsequence are sorted in increasing order.

Let a[0,1,2...n] be the input array, there are two possibilities for every item, whether the ith element is included in
 msis, or not included.
"""


def msis_recur(arr, i, n, prev, s):
    if i == n:
        return s
    # case 1 the ith item excluded
    excl = msis_recur(arr, i + 1, n, prev, s)
    # case 2 the ith item included
    incl = s
    if arr[i] > prev:
        incl = msis_recur(arr, i + 1, n, arr[i], s + arr[i])
    return max(excl, incl)


def msis_dp(arr, n):
    t = [0] * n
    # base case
    t[0] = arr[0]
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and t[i] < arr[i] + t[j]:
                t[i] = arr[i] + t[j]
    return max(t)


arr = [10, 15, 9, 12, 17, 14]
print(msis_recur(arr, 0, len(arr), -62727, 0))
print(msis_dp(arr, len(arr)))
