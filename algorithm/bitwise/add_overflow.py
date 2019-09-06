"""
Check for integer overflow.
"""


def add_overflow(a, b):
    if a > 0xffffffff-b:
        return -1
    print(a+b)
    return 0


print(add_overflow(100000, -1000))
print(add_overflow(0xfffffff1, 15))