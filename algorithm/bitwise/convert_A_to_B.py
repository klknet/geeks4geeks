"""
Count number of bits to be flipped to convert A to B.
"""


def count(a, b):
    c = 0
    a_xor_b = a ^ b
    while a_xor_b:
        if a_xor_b & 1:
            c += 1
        a_xor_b >>= 1
    return c


def smallest_power_of_2(n):
    if n and not n & n - 1:
        return n
    c = 0
    while n != 0:
        c += 1
        n >>= 1
    return 1 << c


def next_power_of_2(n):
    n = n - 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1


print(count(10, 20))
print(count(7, 10))
print(smallest_power_of_2(0))
print(smallest_power_of_2(5))
print(smallest_power_of_2(16))
print(smallest_power_of_2(17))
print(next_power_of_2(1))
print(next_power_of_2(5))
print(next_power_of_2(17))
