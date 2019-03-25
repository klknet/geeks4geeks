"""
Given a positive integer N, count all possible distinct binary string of length N such that there are no consecutive 1's
Let a[i] be the number of binary strings of length i which do not contains any two consecutive 1's and which end in 0.
Similarly, let b[i] be the number of such strings which end in 1. We can append either 0 or 1 to a string ending in 0,
but we can only append 0 to a string ending in 1. This yields the recurrence relation.
a[i] = a[i-1]+b[i-1]
b[i] = a[i-1]
"""


def count_strings(n):
    a = [0] * n
    b = [0] * n
    a[0] = b[0] = 1
    for i in range(1, n):
        # a[i] i'th is 0
        a[i] = a[i - 1] + b[i - 1]
        # b[i] i'th is 1
        b[i] = a[i - 1]
    return a[n - 1] + b[n - 1]


def count_strings_easy(n):
    return (2 ** n) - n*(n - 1) // 2


for i in range(1, 8):
    # print('dp', count_strings(i))
    print('easy', count_strings_easy(i))
