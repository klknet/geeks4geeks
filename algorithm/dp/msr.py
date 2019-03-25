"""
Maximum sum rectangle.
Given a 2D array, find the maximum sum subarray in it.
Maximum sum rectangle.
Given a 2D array, find the maximum sum subarray in it.
The idea is to fix the left and right columns one by one and find the maximum contiguous rows for every left and right
column pair. We basically find top and bottom row numbers(which have maximum sum) for every fixed left and right column
pair. To find the top and bottom row numbers, calculate sum of elements in every row from left to right and store these
sums in an array say temp[]. So temp[i] indicates sum of elements from left to right in row i. If we apply kadane's 1D
algorithm on temp[], and get the maximum sum subarray of temp, this maximum sum would be the maximum possible sum with
left and right as boundary columns. To get the overall maximum sum, we compare this sum with the maximum sum so far.
"""

import algorithm.dp.lscs as lscs


def msr(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = 0
    temp = [0] * m
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                temp[k] = sum(matrix[k][i:j + 1])
            s, top, bottom = lscs.max_subarray_sum(temp)
            max_sum = max(max_sum, s)
    return max_sum


m = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
print(msr(m))
