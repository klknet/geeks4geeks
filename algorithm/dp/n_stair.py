"""
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs
at a time. Count the number of ways, the person can reach the top.
ways(n) = ways(n-1)+ways(n-2)
"""


def n_stair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for i in range(3, n + 1):
        res = a + b
        a = b
        b = res
    return res


print(n_stair(10))
