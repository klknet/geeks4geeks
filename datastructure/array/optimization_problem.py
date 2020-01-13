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


def buy_sell_share_atmost_twice(arr):
    """
    Maximum profit by buying and selling a share at most twice.
    :param arr:
    :return:
    """
    profit = [0] * len(arr)
    max_price = arr[-1]
    # calculate maximum profit at one transaction in subarray [i,n]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_price:
            max_price = arr[i]
        profit[i] = max(profit[i+1], max_price-arr[i])
    min_price = arr[0]
    # calculate maximum profit at two transaction
    for i in range(1, len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        # Maximum profit is maximum of:
        # 1) previous maximum, i.e., profit[i-1]
        # 2) (Buy, Sell) at (min_price, arr[i]) and add profit at other transaction. stored in profit[i]
        profit[i] = max(profit[i-1], profit[i]+(arr[i]-min_price))
    return profit[-1]


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print('Maximum contiguous sum is', largest_sum_subarray(arr))
    arr = [2, 30, 15, 10, 8, 25, 80]
    print("Max profit", buy_sell_share_atmost_twice(arr))
