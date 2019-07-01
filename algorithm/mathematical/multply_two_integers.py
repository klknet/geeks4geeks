"""
Multiply two integers without multiplication, division, and bitwise operations and no loop.
"""


def multiply_util(x, y):
    res = 0
    if y > 0:
        res = multiply_util(x, y - 1) + x
    return res


def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    res = multiply_util(abs(x), abs(y))
    if (x < 0 < y) or (x > 0 > y):
        return -res
    return res


print(multiply(3, -5))
