"""
calculate x^y
"""


def pow(x, y):
    if y == 0:
        return 1
    temp = pow(x, int(y / 2))
    if y & 1 == 0:
        return temp * temp
    else:
        return x * temp * temp if y > 0 else temp * temp / x


def quick_pow(x, y):
    """
    x^y can write as x^(1*2^0+0*2^1+1*2^2...) using binary of y.
    then if current bit is 1, multiply curent base to the result. base(n)=base(n-1)^2
    :param x:
    :param y:
    :return:
    """
    res = 1
    base = x if y > 0 else 1 / x
    while y != 0:
        if y & 1 == 1:
            res *= base
        base *= base
        y = int(y / 2)
    return res


x, y = 5, 9
print(pow(x, y))
# print(quick_pow(x, y))
print(pow(2, -3))
print(quick_pow(2, -3))
