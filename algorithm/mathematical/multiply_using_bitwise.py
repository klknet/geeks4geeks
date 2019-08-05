"""
Multiply two numbers using bitwise operators.
Let the two numbers as 'a' and 'b'.
1)Initialize result res as 0.
2)Do following while b is greater than 0.
    a)If b is odd, add a to res.
    b)Double a and halve b.
3)return res.
"""


def multiply(a, b):
    res = 0
    while b > 0:
        if b & 1 == 1:
            res += a
        a = a << 1
        b = b >> 1
    return res


print(multiply(3, 5))
print(multiply(18, 1))
