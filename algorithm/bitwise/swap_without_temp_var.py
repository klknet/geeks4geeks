"""
How to swap two numbers without a temporary variable.
"""


def swap(a, b):
    if a == b:
        return
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


def swap1(a, b):
    if a == b:
        return
    a = a * b
    b = a / b
    a = a / b
    print(a, b)


def swap2(a, b):
    if a == b:
        return
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)


a, b = 3, 7
swap(a, b)
swap1(a, b)
swap2(a, b)
