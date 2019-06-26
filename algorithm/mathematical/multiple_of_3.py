"""
Write an efficient function to check if a number is multiple of 3.
"""


def multiple_of_3(n):
    odd_count = 0
    even_count = 0
    n = abs(n)
    if n == 0:
        return 1
    if n == 1:
        return 0
    while n > 0:
        if n & 1:
            even_count += 1
        if n & 2:
            odd_count += 1
        n >>= 2
    return multiple_of_3(odd_count - even_count)


def multiply_by_seven(n):
    return (n << 3) - n


print(multiple_of_3(24))
print(multiply_by_seven(6))
