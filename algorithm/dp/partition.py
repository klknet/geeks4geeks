"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements
in both subsets is same.
Following are two main steps to solve this problem.
1)Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
2)If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.
"""


def is_subset_sum(arr, n, s):
    if s == 0:
        return True
    if n > 0:
        return is_subset_sum(arr, n - 1, s) or is_subset_sum(arr, n - 1, s - arr[n - 1])
    return False


def partition(arr):
    s = sum(arr)
    if s % 2 == 1:
        return False
    return is_subset_sum(arr, len(arr), s / 2)


def partition_dp(arr):
    s = sum(arr)
    n = len(arr)
    if s % 2 == 1:
        return False
    s = s // 2
    # build a s//2*n matrix
    p = [[False for i in range(n+1)] for j in range(s+1)]
    for i in range(0, s + 1):
        for j in range(1, n+1):
            if i == 0:
                p[i][j] = True
            else:
                p[i][j] = p[i][j-1]
                if i >= arr[j-1]:
                    p[i][j] = p[i][j-1] or p[i - arr[j-1]][j - 1]
    return p[s][n]


arr = [10, 5, 2, 15, 2, 2, 2]
arr = [3, 1, 1, 2, 2, 1]
print(partition(arr))
print(partition_dp(arr))
