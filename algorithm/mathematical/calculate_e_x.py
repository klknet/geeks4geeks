"""
Efficient program to calculate e^x.
The value of Exponential Function e^x can be expressed using following Taylor Series.
e^x = 1 + x/1! + x^2/2! + x^3/3! + ... + x^n/n!
The series can be re-written as
e^x = 1 + x/1 (1 + x/2 (1 + x/3(......)))
so we must calculate s(1)
s(n-1) = 1 + x/n-1 * s(n)
"""


def e_power_of_x(x, n):
    s = 1.0
    for i in range(n - 1, 0, -1):
        s = 1 + s * x / i
    return s


print(e_power_of_x(1, 20))
