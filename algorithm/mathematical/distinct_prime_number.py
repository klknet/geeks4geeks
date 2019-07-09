"""
Number which has the maximum number of distinct prime factors in the range M to N.
Create a factorCount[] array to store the number of distinct prime factors of a number. While marking the number as prime,
increment the count of prime factor in its multiples. In the end, get the maximum number stored in factorCount[] array
which will be the answer.
"""
import math


def max_distinct_prime_num(m, n):
    prime = [True] * (n + 1)
    factor = [0] * (n + 1)
    for i in range(2, n//2 + 1):
        if prime[i]:
            prime[i] += 1
            for j in range(i * 2, n + 1, i):
                prime[j] = False
                factor[j] += 1
    max_d = -1
    idx = -1
    for i in range(m, n + 1):
        if factor[i] > max_d:
            max_d = factor[i]
            idx = i
    print('maximum distinct number is', idx, 'count is', max_d)


max_distinct_prime_num(100, 150)
