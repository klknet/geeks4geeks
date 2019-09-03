"""
Multiply a given number with 3.5.
"""


def multiply_with_3_point_5(n):
    return (n << 2) - (n >> 1)


def turn_off_rightmost(n):
    return n & (n - 1)


n = -4
print(multiply_with_3_point_5(n), n * 3.5)
print(turn_off_rightmost(12))
