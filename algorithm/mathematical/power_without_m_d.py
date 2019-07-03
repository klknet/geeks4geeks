"""
Write your owe Power without multiplication(*) and division(/) operators.
"""


def power(x, y):
    if y == 0:
        return 1
    res = 1
    for i in range(y):
        base = 0
        for j in range(x):
            base += res
        res = base
    return res


def power2(x, y):
    if y == 0:
        return 1
    return multiply(power2(x, y - 1), x)


def multiply(a, b):
    if b == 0:
        return 0
    return multiply(a, b - 1) + a


x, y = 3, 7
print(power(x, y))
print(power2(x, y))
