"""
Problem:
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S={S1, S2, ..., Sm} valued
coins, how many ways we can make the change? The order of coins doesn't matter.

Solution:
To count the total number of solutions, we can divide all set solutions into two sets.
1)Solutions that not contain mth coin.
2)Solutions that contain at least one mth coin.
Let count(S[], m, n) be the function to count the number of solutions, then count(S[], m, n) can be written as sum of
count(S[], m-1, n) and count(S[], m, n-Sm)

Therefore, the problem has optimal substructure property as the problem can be solved using solutions to subproblems.
"""


def count(s, m, n):
    # If n is zero, there is only one solution(do not include any coin).
    if n == 0:
        return 1
    # If n is smaller than 0, then no solution exists.
    if n < 0:
        return 0
    # If there are no coins and n is greater than zero, then no solution exists.
    if m <= 0 and n >= 1:
        return 0
    return count(s, m - 1, n) + count(s, m, n - s[m - 1])


def count_dp(s, m, n):
    t = [[0] * (n + 1) for i in range(m)]

    for i in range(m):
        for j in range(n + 1):
            if j == 0:
                t[i][0] = 1
            else:
                # not contain ith coin
                x = t[i - 1][j] if i > 0 else 0
                # contain ith coin
                y = t[i][j - s[i]] if j - s[i] >= 0 else 0
                t[i][j] = x + y

    return t[m - 1][n]


def count_dp_opt(s, m, n):
    t = [0] * (n + 1)
    # base case, zero only has 1 solution
    t[0] = 1
    for i in range(m):
        for j in range(s[i], n + 1):
            t[j] += t[j - s[i]]
    return t[n]


arr = [1, 2, 3]
arr = [3, 2, 1, 5]
n = 9
print(count(arr, len(arr), n))
print(count_dp(arr, len(arr), n))
print(count_dp_opt(arr, len(arr), n))
