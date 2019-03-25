"""
Largest sum contiguous subarray.
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has
the largest sum.
Simple idea of the Kadane's algorithm is to look for all positive contiguous segments of the array(max_ending_here is used
for this). And keep track of maximum sum contiguous segment among all positive contiguous segments(max_so_far is used for
this). Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far.
"""

import sys


def max_subarray_sum(arr):
    max_ending_here = max_so_far = -sys.maxsize
    s = i = j = 0
    for x in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[x]
        # the ending index of maximum sum
        if max_ending_here > max_so_far:
            i = s
            j = x
            max_so_far = max_ending_here
        # begin the new segment
        if max_ending_here < 0:
            s = x + 1
            max_ending_here = 0
    return max_so_far, i, j


a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [-3, 3, 19, 7]
print(max_subarray_sum(a))
