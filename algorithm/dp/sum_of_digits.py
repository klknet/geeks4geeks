"""
Compute sum of digits in all numbers from 1 to n.
Given a number n, find sum of digits in all numbers from 1 to n.
In general, we can compute sum(10^d-1) using below formula
sum(10^d -1) = 10*sum(10^(d-1) -1) + 45*10^(d-1)
1)Find the number of digits minus one in n. Let this value be 'd'. For 328, d=2
2)Compute some of digits in numbers from 1 to 10^d -1. Let this sum be w. For 328, we compute sum of digits from 1 to 99
using above formula.
3)Find most significant digit (msd) in n. For 328 msd is 3.
4)Overall sum is sum of following terms.
    a)Sum of digits in 1 to msd*10^d -1. For 328, sum of digits in numbers from 1 to 299.
    In general, msd*w + 10^d*(1+2+..+msd-1)
    b)Sum of digits in msd*10^d to n. For 328, sum of digits in 300 to 328.
    msd*(n%10^d+1) + sumOfDigits(n%10^d)
"""

import math


def sum_of_digits(n):
    d = math.floor(math.log10(n))
    a = [0]*(d+1)
    a[1] = 45
    # a[1] 1-9
    # a[2] 1-99
    # a[3] 1-999
    for i in range(2, d+1):
        a[i] = a[i-1]*10+10**(i-1)*45
    return sum_of_digits_util(n, a)


def sum_of_digits_util(n, a):
    if n<10:
        return n*(1+n)//2
    d = math.floor(math.log10(n))
    p = 10 ** d
    msd = n // p
    return msd * a[d] + msd * (msd - 1) // 2 * p + (n % p + 1) * msd + sum_of_digits_util(n % p, a)


print(sum_of_digits(18))
