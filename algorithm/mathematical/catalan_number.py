"""
Program for nth Catalan number.
"""


def nth_catalan(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += nth_catalan(i) * nth_catalan(n - 1 - i)
    return res


def nth_catalan_dp(n, t):
    if n <= 1:
        return 1
    if t[n] != 0:
        return t[n]
    res = 0
    for i in range(n):
        res += nth_catalan_dp(n - i - 1, t) * nth_catalan_dp(i, t)
    t[n] = res
    return t[n]


# using formula C(n) = 1/(n+1) (2n!)/n!
def nth_catalan_formula(n):
    return _nchoosek(2 * n, n) // (n + 1)


def _nchoosek(n, k):
    if k > n / 2:
        k = n - k
    res = 1
    for i in range(1, k + 1):
        res *= n - i + 1
        res //= i
    return res


for i in range(10):
    print(i, nth_catalan(i))
    print(i, nth_catalan_dp(i, (i + 1) * [0]))
    print(i, nth_catalan_formula(i))
