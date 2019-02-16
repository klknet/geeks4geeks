"""
Given a cost matrix cost[][] and position (m,n) in cost[][], write a function that returns cost of minimum cost path to
reach (m,n) from (0,0).
1)optimal substructure properties
The path to reach (m,n) must be through one of 3 cells: (m-1,n), (m,n-1), (m-1,n-1), So minimum cost to reach (m,n) can
be written as "minimum of 3 cells plus cost[m][n]"
minCost(m,n) = cost[m][n]+min(minCost(m-1,n), minCost(m,n-1), minCost(m-1,n-1))
"""

import sys

count = 0


def mcp_recur(cost, m, n):
    global count
    count += 1
    if m == 0 and n == 0:
        return cost[m][n]
    if m < 0 or n < 0:
        return sys.maxsize
    return cost[m][n] + min(mcp_recur(cost, m - 1, n), mcp_recur(cost, m, n - 1), mcp_recur(cost, m - 1, n - 1))


def mcp_dp(cost, m, n):
    global count
    count = 0
    mcp = [[0] * (n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            count += 1
            if i == 0 and j == 0:
                mcp[i][j] = cost[i][j]
            elif i == 0:
                mcp[i][j] = cost[i][j] + mcp[i][j - 1]
            elif j == 0:
                mcp[i][j] = cost[i][j] + mcp[i - 1][j]
            else:
                mcp[i][j] = cost[i][j] + min(mcp[i - 1][j], mcp[i][j - 1], mcp[i - 1][j - 1])
    return mcp[m-1][n-1]


cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
print(mcp_recur(cost, 2, 2))
print(count)
print(mcp_dp(cost, 3, 3))
print(count)
