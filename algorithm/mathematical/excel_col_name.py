"""
Find excel column name from a given column number.
"""


def column_name(n):
    if n <= 26:
        return chr(ord('A') + n - 1)
    res = ''
    while n > 0:
        r = n % 26
        if r == 0:
            res += 'Z'
            n = int(n / 26) - 1
        else:
            res += chr(ord('A') + r - 1)
            n = int(n / 26)
    return res[::-1]


print(column_name(700))
