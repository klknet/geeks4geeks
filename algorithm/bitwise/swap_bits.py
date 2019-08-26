"""
Swap bits in a given number.
1)Move all bits of the first set to the rightmost side
set1 = (x>>p1) & mask  (mask is 2**n-1)
set2 = (x>>p2) & mask
2)XOR the two set of bits
xor = set1 ^ set2
3)Put the xor bits to the original position.
xor = (xor << p1) | (xor << p2)
4)Finally XOR the xor with the original number so the two sets are swapped.
result = xor ^ x
"""


def swap_bits(x, f, s, n):
    mask = 2 ** n - 1
    first_bits = x >> f & mask
    second_bits = x >> s & mask
    x = ((~(mask << f)) & x) | (second_bits << f)
    x = ((~(mask << s)) & x) | (first_bits << s)
    return x


def swap_bits_2(x, p1, p2, n):
    mask = (1 << n) - 1
    set1 = (x >> p1) & mask
    set2 = (x >> p2) & mask
    xor = set1 ^ set2
    xor = (xor << p1) | (xor << p2)
    return x ^ xor


print(swap_bits(47, 1, 5, 3))
print(swap_bits_2(47, 1, 5, 3))
