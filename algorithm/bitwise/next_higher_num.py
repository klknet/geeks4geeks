"""
Next higher number with same number of set bits.
"""


def next_higher_number(x):
    c = x & -x
    r = c + x
    return (((r ^ x) >> 2)//c) | r


print(next_higher_number(156))
