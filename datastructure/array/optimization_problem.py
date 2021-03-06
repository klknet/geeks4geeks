"""
Optimization Problems.
"""
import sys
import math


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


def buy_sell_share_atmost_twice(arr):
    """
    Maximum profit by buying and selling a share at most twice.
    :param arr:
    :return:
    """
    profit = [0] * len(arr)
    max_price = arr[-1]
    # calculate maximum profit at one transaction in subarray [i,n]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_price:
            max_price = arr[i]
        profit[i] = max(profit[i + 1], max_price - arr[i])
    min_price = arr[0]
    # calculate maximum profit at two transaction
    for i in range(1, len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        # Maximum profit is maximum of:
        # 1) previous maximum, i.e., profit[i-1]
        # 2) (Buy, Sell) at (min_price, arr[i]) and add profit at other transaction. stored in profit[i]
        profit[i] = max(profit[i - 1], profit[i] + (arr[i] - min_price))
    return profit[-1]


def find_subarray_least_average(arr, k):
    """
    Find the subarray with least average.
    Given an array arr[] with size of n and an integer k such that k<=n.
    Using sliding windows.
    :param arr:
    :param k:
    :return:
    """
    res_idx = 0
    min_sum = 0
    for i in range(3):
        min_sum += arr[i]
    curr_sum = min_sum
    for i in range(3, len(arr)):
        curr_sum = curr_sum + arr[i] - arr[i - k]
        if curr_sum < min_sum:
            min_sum = curr_sum
            res_idx = i
    return res_idx - k, min_sum / 3


def minimize_maximum_difference(arr, k):
    n = len(arr)
    if n <= 1:
        return 0
    arr.sort()
    ans = arr[-1] - arr[0]
    big = arr[-1] - k
    small = arr[0] + k
    if small > big:
        small, big = big, small
    for i in range(1, n - 1):
        add = arr[i] + k
        subtract = arr[i] - k
        # If both subtraction and addition don't change diff
        if subtract >= small or add <= big:
            continue
        # Either subtraction causes a smaller number or addition causes a greater number
        # Update small or big using greedy approach.
        if add - small >= big - subtract:
            small = subtract
        else:
            big = add
    return min(ans, big - small)


def min_num_of_jumps(arr, n):
    """
    minJumps(start, end) = min(minJumps(k, end)) for all k reachable from start
    :param arr:
    :param n:
    :return:
    """
    if n == 1:
        return 0
    res = sys.maxsize
    for i in range(n - 2, -1, -1):
        if i + arr[i] >= n - 1:
            jumps = min_num_of_jumps(arr, i + 1)
            if jumps != sys.maxsize:
                res = min(res, jumps + 1)
    return res


def min_jumps_dp(arr):
    """
    using dynamic programming.
    :param arr:
    :return:
    """
    n = len(arr)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = sys.maxsize
        for j in range(i):
            # find the first position that can reach to i
            if j + arr[j] >= i and dp[j] != sys.maxsize:
                dp[i] = min(dp[i], dp[j] + 1)
                break
    return dp[-1]


def length_of_maximum_sum_subarray(arr):
    """
    Find the length of maximum sum of sub array of a given array.
    :param arr:
    :return:
    """
    max_ending_here = 0
    max_so_far = -sys.maxsize
    start = end = 0
    s = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i
            start = s
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    return max_so_far, start, end


def minimum_difference_pair(arr):
    """
    Find the minimum difference between any pair in an unsort array.
    :param arr:
    :return:
    """
    arr.sort()
    res = sys.maxsize
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < res:
            res = arr[i] - arr[i - 1]
    return res


def bitset(a, b):
    """
    Given two integer a and b, find multiple of 2 or 5 between a and b
    Using bitset save space
    :param a:
    :param b:
    :return:
    """
    size = math.ceil((b - a) / 32)
    arr = [0] * size
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 5 == 0:
            setbit(arr, i - a)
    for i in range(a, b + 1):
        if checkbit(arr, i - a):
            print(i, end=" ")


def setbit(arr, idx):
    arr[idx >> 5] |= (1 << (idx & 31))


def checkbit(arr, idx):
    return arr[idx >> 5] & (1 << (idx & 31))


def longest_span_with_same_sum(arr1, arr2):
    """
    Longest span with same sum in two Binary arrays.
    :param arr1:
    :param arr2:
    :return:
    """
    hash = {}
    max_len = 0
    diff = [0] * len(arr1)
    for i in range(len(arr1)):
        diff[i] = arr1[i] - arr2[i]
    s = 0
    for i in range(len(arr1)):
        s += diff[i]
        if s==0:
            max_len = i+1
        if s in hash:
            max_len = max(max_len, i - hash[s])
        else:
            hash[s] = i
    return max_len

max_sum = 0


def _max_sum_incr_seq(arr, n):
    global max_sum
    if n == 1:
        return arr[n - 1]
    res = 0
    for i in range(1, n):
        s = _max_sum_incr_seq(arr, i)
        if arr[i - 1] < arr[n - 1] and s + arr[n - 1] > res:
            res = s + arr[n - 1]
    max_sum = max(max_sum, res)
    return res


def max_sum_incr_seq(arr):
    """
    Maximum Sum Increasing Subsequence.
    :param arr:
    :return:
    """
    global max_sum
    n = len(arr)
    _max_sum_incr_seq(arr, n)
    return max_sum


def max_sum_incr_seq_dp(arr):
    dp = [0] * len(arr)
    for i in range(len(arr)):
        dp[i] = arr[i]
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]
    return max(dp)

if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print('Maximum contiguous sum is', largest_sum_subarray(arr))
    arr = [2, 30, 15, 10, 8, 25, 80]
    print("Max profit", buy_sell_share_atmost_twice(arr))
    arr = [3, 7, 90, 20, 10, 50, 40]
    res = find_subarray_least_average(arr, 3)
    print("Least average is %s at %s position" % (res[1], res[0]))
    arr = [4, 6]
    # print("Minimum difference is", minimize_maximum_difference(arr, 10))
    # arr = [1, 15, 10]
    # print("Minimum difference is", minimize_maximum_difference(arr, 6))
    # arr = [1, 5, 15, 10]
    # print("Minimum difference is", minimize_maximum_difference(arr, 3))
    # arr = [6, 10]
    # print("Minimum difference is", minimize_maximum_difference(arr, 3))
    # arr = [1, 10, 14, 14, 14, 15]
    print("Minimum difference is", minimize_maximum_difference(arr, 6))
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    # arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    print("Minimum jumps to reach end", min_num_of_jumps(arr, len(arr)))
    print("Minimum jumps to reach end", min_jumps_dp(arr))
    arr = [1, 101, 2, 3, 100, 4, 5]
    print("Maximum sum increasing subsequence is", max_sum_incr_seq(arr))
    print("Maximum sum increasing subsequence is", max_sum_incr_seq_dp(arr))

    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum sum of subarray", length_of_maximum_sum_subarray(arr))
    a, b = 2, 10
    print("Multiple of 2 or 5 between %s and %s is" % (a, b))
    bitset(a, b)
    arr1 = [0, 1, 0, 1, 1, 1, 1]
    arr2 = [1, 1, 1, 1, 1, 0, 1]
    print("\nLength of the longest common span with same sum is", longest_span_with_same_sum(arr1, arr2))
