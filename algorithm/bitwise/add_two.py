"""
Add two numbers without using arithmetic operators.
"""


def add_two(x, y):
    while y != 0:
        x, y = x ^ y, (x & y) << 1
    return x


def add_two_recur(x, y):
    if y == 0:
        return x
    return add_two(x ^ y, (x & y) << 1)


def smallest(x, y, z):
    return my_min(x, my_min(y, z))


def my_min(x, y):
    return y + ((x - y) & ((x - y) >> 31))


print(add_two(13, 19))
print(add_two_recur(13, 19))
print(smallest(12, -19, 2))
