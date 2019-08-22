"""
Program for bisection method.
"""


def bisection(a, b):
    e = 0.01
    c = a
    while b - a > e:
        c = (b + a) / 2
        if fun(c) == 0:
            break
        elif fun(c) > 0:
            b = c
        else:
            a = c
    return c


def newton_raphson(x):
    h = fun(x) / derivative(x)
    while abs(h) > 0.001:
        h = fun(x) / derivative(x)
        x -= h
    return x


def derivative(x):
    return 3 * x * x - 2 * x


def fun(x):
    return x ** 3 - x ** 2 + 2


print(bisection(-200, 300))
print(newton_raphson(-20))
