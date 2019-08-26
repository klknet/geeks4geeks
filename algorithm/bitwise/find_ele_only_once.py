"""
Find the element that appears once.
We can sum the bits in same position for all the numbers and take modulo with 3. The bits for which sum is not multiple
of 3, are the bits of number with single occurrence.
"""


def find_once(arr):
    int_size = 32
    res = 0
    for i in range(int_size):
        s = 0
        x = 1 << i
        for j in arr:
            if j & x:
                s += 1
        if s % 3 != 0:
            res |= x
    return res


"""
Detect if two integers have different signs.
"""


def opposite_sign(a, b):
    return True if a ^ b < 0 else False


def opposite_sign_1(a, b):
    return b >= 0 if a < 0 else b < 0


def opposite_sign_2(a, b):
    return ((a ^ b) >> 31) < 0


print(find_once([12, 1, 12, 3, 12, 1, 1, 2, 3, 3]))
print(opposite_sign(-100, 200), opposite_sign_1(-100, 200), opposite_sign_2(-100, 200))
print(opposite_sign(-100, -200), opposite_sign_1(-100, -200), opposite_sign_2(-100, -200))
print(opposite_sign(100, 200), opposite_sign_1(100, 200), opposite_sign_2(100, 200))
