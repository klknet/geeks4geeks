"""
Count trailing zeros in factorial of a number.

Trailing 0s in n! = Count of 5s in prime factors in n!.
                  = floor(n/5) + floor(n/25) + floor(n/125) + ...
"""


def trailing_zeros(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
    return count


print(trailing_zeros(28))
