"""
Find position of the only one set bit.
"""


def position(n):
    if n == 0 or (n & n - 1) != 0:
        return 'valid number'
    pos = 0
    while n != 0:
        pos += 1
        n >>= 1
    return pos


print(position(16))
print(position(128))
print(position(0))
print(position(5))
