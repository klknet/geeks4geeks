"""
Count set bits in integer.
"""


def count(n):
    c = 0
    while n != 0:
        if n & 1:
            c += 1
        n >>= 1
    return c


def count1(n):
    no_of_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    c = 0
    for i in range(8):
        c += no_of_bits[n & (15 >> i * 4)]
    return c


def count2(n):
    c = 0
    while n:
        c += 1
        n &= n - 1
    return c


print(count(13))
print(count1(13))
print(count2(13))
print(count(6))
print(count1(6))
print(count2(6))
