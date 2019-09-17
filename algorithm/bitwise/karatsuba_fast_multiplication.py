"""
Karatsuba algorithm for fast multiplication using Divide and Conquer algorithm.

Using divide and conquer, we can multiply two integers in less than complexity. We divide the given numbers in two halves.
Let the given number be x and y.
x = xl * 2^n/2 + xr
y = yl * 2^n/2 + yr
The product xy can be writen as following.
x*y = 2^n * xl * yl + 2^n/2 * (xl * yr + xr * yl) + xr * yr
xl * yr + xr * yl = (xl + xr) * (yl + yr) - xl * yl - xr * yr
With above tricky, the recurrence becomes T(n) = 3*T(n/2) + O(n) and solution of this recurrence is O(n^log2^3)
"""


def add_bit_set(x, y):
    x, y = append_leading_0(x, y)
    n = len(x)
    carry = 0
    res = ''
    while n > 0:
        n -= 1
        first = ord(x[n]) - ord('0')
        second = ord(y[n]) - ord('0')
        s = first ^ second ^ carry
        res = str(s) + res
        carry = (first & second) | (first & carry) | (second & carry)
    if carry > 0:
        res = '1' + res
    return res


def karatsuba(x, y):
    x, y = append_leading_0(x, y)
    # base case
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return int(x) * int(y)
    n = len(x)
    left = int(n / 2)
    right = n - left
    xl, xr, yl, yr = x[0:right], x[right:], y[0:right], y[right:]
    xl_yl = karatsuba(xl, yl)
    xr_yr = karatsuba(xr, yr)
    xl_xr_yl_yr = karatsuba(add_bit_set(xl, xr), add_bit_set(yl, yr))
    return (xl_yl << left * 2) + ((xl_xr_yl_yr - xl_yl - xr_yr) << left) + xr_yr


def append_leading_0(x, y):
    n1, n2 = len(x), len(y)
    if n1 < n2:
        x = x.zfill(n2)
    elif n1 > n2:
        y = y.zfill(n1)
    return x, y


print(karatsuba('1100', '1010'))
print(karatsuba('110', '1010'))
print(karatsuba('11', '1010'))
print(karatsuba('1', '1010'))
print(karatsuba('0', '1010'))
print(karatsuba('111', '111'))
print(karatsuba('11', '11'))
