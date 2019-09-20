"""
Check if a number is multiple of 9 using bitwise operators.

n/9 = n/8 - n/72

n/8 = floor(n/8) + (n%8)/8
n/9 = floor(n/8) + (n%8)/8 - (floor(n/8) + (n%8)/8)/9
    = floor(n/8) + (floor(n/8) - n%8)/9
From above equation, n is a multiple of 9 only if the expression (floor(n/8） - n%8)/9 is an integer. The sub-expression
can only be an integer if floor
"""


def is_div_of_9(n):
    if n == 0 or n == 9:
        return True
    if n < 9:
        return False
    return is_div_of_9((n >> 3) - (n & 7))


print(is_div_of_9(19))
print(is_div_of_9(72))
