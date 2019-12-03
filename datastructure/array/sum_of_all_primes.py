"""
Sum of all the prime numbers with the count of digits <= D.
"""


def sum_of_prime(d):
    n = 10 ** d
    prime = [True] * n
    for i in range(2, n):
        m = i*i
        if prime[i]:
            while m < n:
                prime[m] = False
                m += i
    s = 0
    for i in range(2, n):
        if prime[i]:
            s += i
    return s


print(sum_of_prime(2))
print(sum_of_prime(3))



