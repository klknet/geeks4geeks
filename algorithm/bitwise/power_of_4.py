"""
Find whether a given number is a power of 4 or not.
"""

"""
Keep dividing the number by 4, if n%4 becomes non-zero and n is not 1 then n is not a power of 4, otherwise n is power
of 4.
"""


def power_of_4(n):
    if n == 0:
        return False
    while n != 1:
        if n % 4 != 0:
            return False
        n = n / 4
    return True


"""
1)There is only one bit set in the binary representation of n.
2)The count of zero bits before the only set bit is even.
"""


def power_of_4_1(n):
    if n < 4:
        return False
    INT_BIT = 32
    c = 0
    zero = 0
    for i in range(INT_BIT):
        if n & 1 == 1:
            c += 1
        elif c < 1:
            zero += 1
        n >>= 1
    return c == 1 and zero & 1 == 0


"""
1)There is only one bit set in the binary representation of n.
2)The bits & 0xAAAAAAAA is zero
"""


def power_of_4_2(n):
    return n != 0 and not (n & (n - 1)) and not (n & int('0xAAAAAAAA', 16))


def abs_(n):
    mask = n >> 31
    return mask ^ (n + mask)


print(power_of_4(64))
print(power_of_4_1(16))
print(power_of_4_2(16))
print(abs_(-6))
