"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to
given sum.
Let f(i, s) be the if the arr[0..i] have a subset with sum equal to s, then it can write in following formula
f(i, s) = f(i-1, s) or f(i-1, s-a[i])
"""


def equal_2_sum(arr, i, s):
    if s == 0:
        return True
    if i == 0 and s != 0:
        return False
    if arr[i - 1] > s:
        return equal_2_sum(arr, i - 1, s)
    return equal_2_sum(arr, i - 1, s) or equal_2_sum(arr, i - 1, s - arr[i - 1])


# Pseudo-Polynomial-Algorithm
def equal_2_sum_dp(arr, s):
    # t[i][j] represents if there is a subset of a[0..j] with sum equal to i
    n = len(arr)
    t = [[False for col in range(n+1)] for row in range(s + 1)]
    for i in range(s + 1):
        for j in range(1, n+1):
            if i == 0:
                t[i][j] = True
            elif i >= arr[j-1]:
                t[i][j] = t[i - arr[j-1]][j - 1] or t[i][j - 1]
            elif i < arr[j-1]:
                t[i][j] = t[i][j-1]
    return t[s][n]


arr = [3, 5, 1, 4, 12]
s = 6
print(equal_2_sum(arr, len(arr), s))
print(equal_2_sum_dp(arr, s))
