"""
Position of rightmost set bit.
"""

import math


def position(n):
    return math.log2(n & -n) + 1


def binary_rep(n):
    res = []
    while n != 0:
        res.insert(0, str(n & 1))
        n >>= 1
    return ''.join(res)


print(position(18))
print(binary_rep(169))
