"""
Horner's method for polynomial evaluation.

Horner's method can be used to evaluate polynomial in O(n) time. To understand the method, let us consider the example of
2x^3 - 6x^2 + 2x -1. The polynomial can be evaluated as ((2x-6)x+2)x-1. The idea is to initialize result as coefficient
of x^n which is 2 in this case, repeatedly multiply result with x and add next coefficient to result. Finally return result.
"""


def poly_eval(poly, x):
    res = poly[0]
    for i in range(1, len(poly)):
        res = res * x + poly[i]
    return res


print(poly_eval([2, -6, 2, -1], 3))
