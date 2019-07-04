"""
Count numbers that don't contain 3
"""


def count(n):
    if n < 3:
        return n
    if n == 3:
        return 2
    if 3 < n < 10:
        return n - 1
    msd = 0
    d = 0
    t = n
    while t // 10 != 0:
        t = t // 10
        msd = t % 10
        d += 1
    return count(n-msd*(10**d)) + count(msd)*(9**d)


print(count(578))