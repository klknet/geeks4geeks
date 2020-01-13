"""
Optimization Problems.
"""
import sys


def largest_sum_subarray(arr):
    """
    Largest Contiguous Sum Subarray.
    Initialize
        max_ending_here=0
        max_so_far=-inf
    Loop for each element of the array
        1)max_ending_here += arr[i]
        2)if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        3)if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
    :param arr:
    :return:
    """
    max_ending_here = 0
    max_so_far = -sys.maxsize
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print('Maximum contiguous sum is', largest_sum_subarray(arr))
