"""
A number can always be represents as a sum of squares of other numbers. Note that 1 is a square and we can always break
a number as (1*1+1*1+1*1+...). Given a number n, find the minimum number of squares that sum to X.
The idea is simple, we start from 1 and go till a number whose sum is smaller than or equal to n. For every number x, we
recur for n-x.
"""


def get_min_number(n):
    # base case
    if n <= 3:
        return n
    res = n  # the number is n in worst case
    for i in range(2, n):
        temp = i * i
        if temp > n:
            break
        else:
            res = min(res, 1 + get_min_number(n - temp))
    return res


def get_min_util(n, t):
    if n <= 3:
        return n
    if t[n] != 0:
        return t[n]
    res = n
    for i in range(2, n):
        temp = i * i
        if temp > n:
            break
        else:
            res = min(res, 1 + get_min_util(n - temp, t))
    t[n] = res
    return res


def get_min_dp(n):
    # base case
    dp = [0, 1, 2, 3]
    for i in range(4, n+1):
        dp.append(i)
        for j in range(1, i+1):
            temp = j*j
            if temp>i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i-temp])
    return dp[n]


n = 101
print(get_min_dp(n))
# print(get_min_number(n))
