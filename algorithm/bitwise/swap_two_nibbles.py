"""
Swap two nibbles in a byte.
"""


def swap_nibble(n):
    left_nibble = 0xf0f0f0f0 & n
    right_nibble = 0x0f0f0f0f & n
    return (left_nibble >> 4) | (right_nibble << 4)


def turn_off_bit(n, k):
    return n ^ (1 << (k - 1))


def is_palindrome(n):
    l = 31
    r = 0
    while l > r:
        if (n & 1 << l) >> l != (n & 1 << r) >> r:
            return False
        l -= 1
        r += 1
    return True


print(swap_nibble(100))
print(turn_off_bit(15, 4))
print(is_palindrome((1 << 31) + 2))
