"""
Write a program to add two numbers in base 14.
Just add the numbers in base 14 in same way we add in base 10. Add numerals of both numbers one by one from right to left.
If there is a carry while adding two numerals, consider the carry for next numerals.
"""


def add_num(s1, s2):
    n1, n2 = len(s1), len(s2)
    carry = 0
    res = ''
    i, j = n1 - 1, n2 - 1
    while i >= 0 and j >= 0:
        c1 = to_decimal(s1[i])
        c2 = to_decimal(s2[j])
        i -= 1
        j -= 1
        cur = c1 + c2 + carry
        carry = 1 if cur > 13 else 0
        if carry > 0:
            cur = cur - 14
        res = str(to_char(cur)) + res
    while i >= 0:
        cur = to_decimal(s1[i]) + carry
        i -= 1
        carry = 1 if cur > 13 else 0
        if carry > 0:
            cur = cur - 14
        res = str(to_char(cur)) + res
    while j >= 0:
        cur = to_decimal(s2[i]) + carry
        j -= 1
        carry = 1 if cur > 13 else 0
        if carry > 0:
            cur = cur - 14
        res = str(to_char(cur)) + res
    if carry > 0:
        res = '1' + res
    return res


def to_decimal(c):
    if ord('0') <= ord(c) <= ord('9'):
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10


def to_char(c):
    if c >= 10:
        return chr(c - 10 + ord('A'))
    return str(c)


print(add_num('DD12A', 'CD3'))
