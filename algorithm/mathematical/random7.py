"""
Generate integer from 1 to 7 with equal probability.
"""
import random


def range7():
    r = 5 * foo() + foo() - 5
    if r < 22:
        return r % 7 + 1
    return range7()


def foo():
    return random.randint(1, 5)


print(range7())
