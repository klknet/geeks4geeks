"""
Reverse bits of a number.
"""


def reverse1(n):
    new_num = 0
    for i in range(32):
        if n & (1 << i):
            new_num |= (1 << 31 - i)
    return new_num


def reverse(n):
    count = 31
    new_num = n
    n >>= 1
    while n:
        count -= 1
        new_num << 1
        new_num |= n & 1
        n >>= 1
    new_num <<= count
    return new_num


print(reverse(3))
print(reverse1(3))
