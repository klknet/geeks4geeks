"""
Find minimum number of coins that make a given value.
The minimum number of coins for a value v can be computed using below formula:
If v=0 then 0 coin required
If v>0, then
 minCoin(coins[0,...,m-1], v) = min(1+minCoin(coins[0,..,m-1], v-coins[i])
 where i varies from 0 to m-1 and v>=coin[i]
"""

import sys


def min_num_coin(v, arr, n):
    if v == 0:
        return 0
    m = sys.maxsize
    for i in range(n):
        if v >= arr[i]:
            c = min_num_coin(v - arr[i], arr, n)
            if c != sys.maxsize:
                c += 1
            m = min(m, c)
    return m


def min_coin_dp(v, arr):
    n = len(arr)
    dp = [0] * (v + 1)
    return min_coin_util(v, arr, dp)


def min_coin_util(v, arr, dp):
    if v == 0:
        return 0
    if dp[v] > 0:
        return dp[v]
    n = len(arr)
    m = sys.maxsize
    for i in arr:
        if v>=i:
            c = min_coin_util(v-i, arr, dp)
            if c != sys.maxsize:
                c += 1
            m = min(m, c)
    dp[v] = m
    return m


a = [25, 10, 5]
a = [9, 6, 5, 1]
# a = [1, 5, 6, 9]
n = 40
# n = 11
print(min_coin_dp(n, a))
print(min_num_coin(n, a, len(a)))
