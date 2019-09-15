"""
Program to find parity.
Multiply with 7.
"""


def parity(n):
    p = True
    c = 0
    while n:
        c += 1
        p = not p
        n = n & n - 1
    print('Number of 1 bits is', c, ',parity is', 'even' if p else 'odd')


def multiply_with_7(n):
    return (n << 3) - n


def is_power_of_2(n):
    return False if n == 0 or n & n - 1 else True


parity(15)
print(multiply_with_7(10))
print(is_power_of_2(5))
print(is_power_of_2(32))
print(is_power_of_2(0))
