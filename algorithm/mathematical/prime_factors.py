"""
Efficient program to print all prime factors of a given number.
1)While n is divisible by 2, print 2 and divide n by 2.
2)After step 1, n must be odd. Now start a loop from i=3 to square root of n. While i divides n, print i and divide n by
i, increment i by 2 and continue.
3)If n is a prime number and great than 2, then n will not become 1 by above two steps. So print n if it is great than 2.
"""
import math


def prime_factors(n):
    while n & 1 == 0:
        print(2, end=' ')
        n = (n >> 1)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = int(n / i)
            print(i, end=' ')
    # This condition is to handle the case when n is a prime number and great than 2.
    if n>2:
        print(n, end=' ')


prime_factors(5)
