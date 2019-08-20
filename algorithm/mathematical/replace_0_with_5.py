"""
Replace all '0' with '5' in an input integer.
Use of array to store all digits are not allowed.
"""


def replace(n):
    res = n
    base = 1
    if n == 0:
        return 5
    while n > 0:
        if n % 10 == 0:
            res += base * 5
        base *= 10
        n = int(n / 10)
    return res


def convert(n):
    if n == 0:
        return 0
    digit = n % 10
    if digit == 0:
        digit = 5
    return convert(int(n / 10))*10 + digit


print(replace(102))
print(replace(1020))
print(convert(1020))
