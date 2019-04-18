"""
Find the minimum cost to reach destination using a train.
There are N stations on route of a train. The train goes from station 0 to N-1. The ticket cost for all pair of stations
(i,j) is giving where j is greater than i. Find the minimum cost to reach the destination.

minCost(0, N-1) = min( cost[0][n-1], cost[0][1]+minCost(1,N-1), cost[0][2]+minCost(2,N-1), ...,
cost[0][n-2]+minCost(n-2,n-1) )
"""

import sys


def min_cost(cost, i, j):
    if i == j or i == j - 1:
        return cost[i][j]
    min_v = sys.maxsize
    for k in range(i + 1, j + 1):
        curr = cost[i][k] + min_cost(cost, k, j)
        min_v = min(curr, min_v)
    return min_v


def min_cost_dp(cost):
    dp = [0] * len(cost)
    for i in range(1, len(cost)):
        min_v = sys.maxsize
        for j in range(i):
            curr = dp[j] + cost[j][i]
            min_v = min(min_v, curr)
        dp[i] = min_v
    return dp[-1]


def min_cost_dp1(cost):
    n = len(cost)
    dist = [999999]*n
    dist[0] = 0
    for i in range(n):
        for j in range(i+1, n):
            if dist[j] > dist[i] + cost[i][j]:
                dist[j] = dist[i] + cost[i][j]
    return dist[-1]


c = [[0, 15, 80, 90],
     [float("inf"), 0, 40, 50],
     [float("inf"), float("inf"), 0, 70],
     [float("inf"), float("inf"), float("inf"), 0]
     ]
print(min_cost(c, 0, len(c) - 1))
print(min_cost_dp(c))
print(min_cost_dp1(c))
