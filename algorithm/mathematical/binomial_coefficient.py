"""
Binomial Coefficient.
"""


def b_c(n, k):
    if k == 0 or k == n:
        return 1
    if k > n-k:
        k = n-k
    res = 1
    for i in range(k):
        res *= n-i
        res //= i+1
    return res


print(b_c(8, 2))