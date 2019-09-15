"""
Write an Efficient Method to check if a number is Multiple of 3.
"""


def multiple_of_3(n):
    diff = 0
    n = abs(n)
    while n:
        if n & 1:
            diff += 1
        if n & 2:
            diff -= 1
        n >>= 2
    return diff % 3 == 0


print(multiple_of_3(33))
