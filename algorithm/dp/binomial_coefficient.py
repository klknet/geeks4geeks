"""
Following are common definition of Binomial Coefficient
1)A binomial coefficient C(n, k) can be defined as the coefficient of X^k in the expansion of (1+X)^n
2)A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen from
among n objects; More formally, the number of k-element subsets of an n-element set.

The value of C(n,k) can be recursively calculated using following formula for Binomial Coefficients.
C(n,k) = C(n-1,k-1) + C(n-1,k)
C(n,0) = C(n,n) = 1
"""


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


def binomial_coefficient_dp(n, k):
    t = [[0] * (k + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                t[i][j] = 1
            else:
                t[i][j] = t[i - 1][j - 1] + t[i - 1][j]
    return t[n][k]


print(binomial_coefficient(10, 4))
print(binomial_coefficient_dp(10, 4))
