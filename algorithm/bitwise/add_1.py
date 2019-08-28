"""
Add 1 to a given number.
"""

"""
Flip all the bits after the rightmost 0 bit, flip the rightmost 0 bit also get the answer.
"""


def add_1(n):
    mask = 1
    while n & mask:
        n &= mask
        mask << 1
    n ^= mask
    return n


"""
-n = ~n + 1
~n = -n - 1 = -(n+1)
-(~n) = n+1
"""


def add_1_(n):
    return -(~n)


print(add_1(-12))
print(add_1_(-12))
