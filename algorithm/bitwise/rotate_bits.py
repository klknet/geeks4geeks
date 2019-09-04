"""
Rotate bits of a number.
"""


def right_rotate(n, b):
    return (n >> b) | (n << (32 - b)) & 0xffffffff


def left_rotate(n, b):
    return (n << b) | (n >> 32 - b)


n, b = 16, 2
print('right rotate of', n, 'by', b, 'is', right_rotate(n, b))
print('left rotate of', n, 'by', b, 'is', left_rotate(n, b))
