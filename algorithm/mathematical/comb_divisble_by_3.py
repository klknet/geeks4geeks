"""
Count all possible groups of size 2 or 3 that have sum as multiple of 3.
"""


def divisible_by_3(arr):
    c = [0] * 3
    for i in arr:
        c[i % 3] += 1
    res = 0
    # for group of size 2.
    c1 = (c[0] * (c[0] - 1)) >> 1
    c2 = c[1] * c[2]
    # for group of size 3.
    c3 = c[0] * c[1] * c[2]
    c4 = c[0] * (c[0] - 1) * (c[0] - 2) / 6
    c5 = c[2] * (c[2] - 1) * (c[2] - 2) / 6
    c6 = c[1] * (c[1] - 1) * (c[1] - 2) / 6
    return c1 + c2 + c3 + c4 + c5 + c6


arr = [3, 6, 7, 2, 9]
print((divisible_by_3(arr)))