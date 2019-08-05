"""
How to check a given number is a fibonacci number.
"""
import math


def is_fibonacci_num(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root ** 2 == n

for i in range(1, 10, 1):
    print(i, is_fibonacci_num(i))
