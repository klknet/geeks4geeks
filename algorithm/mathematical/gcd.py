"""
Greatest common divisor.
阿几里德求最大公约数
"""


def gcd(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return x


print(gcd(49, 35))
