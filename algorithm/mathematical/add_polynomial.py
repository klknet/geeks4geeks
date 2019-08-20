"""
Program to add two polynomials.
"""


def add_poly(a, b):
    m, n = len(a), len(b)
    c = max(m, n)
    res = [0] * c
    for i in range(m):
        res[i] += a[i]
    for i in range(n):
        res[i] += b[i]
    return res


def print_poly(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
        if i != 0:
            print('x^'+str(i), end="")
        if i != len(arr)-1:
            print('+', end=" ")
    print()


print_poly(add_poly([5, 0, 10, 6], [1, 2, 4]))
