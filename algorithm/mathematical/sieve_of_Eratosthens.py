"""
Sieve of Eratosthenes.
1.Create a list of consecutive integers from 2 to n(2,3,4..n).
2.Initially, let p equal 2, the first prime number.
3.Starting from p^2, count up in increments of p and mark each of there numbers great than or equal to p^2 itself in the
list. These numbers will be p(p+1), p(p+2), p(p+3),etc...
4.Find the first number great than p in the list that is not marked. If there is no such number, stop. Otherwise, let p
equal this number(the next prime number). and repeat from step 3.
"""
import math
import time


def count_prime(n):
    if n < 2:
        return 0
    if n < 5:
        return 2
    i = 1
    c = 2
    primes = [2, 3]
    while 6 * i < n:
        left_side = 6 * i - 1
        right_side = 6 * i + 1
        if isPrime(left_side):
            primes.append(6 * i - 1)
            c += 1
        if right_side < n and isPrime(right_side):
            primes.append(right_side)
            c += 1
        i += 1
    print(primes)
    print(c)


def isPrime(n):
    r = int(math.sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_Eratosthens(n):
    if n < 2:
        return
    prime = [1] * n
    prime[0] = prime[1] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if prime[i] == 1:
            for j in range(i * i, n, i):
                prime[j] = 0
    print(sum(prime))
    for i in range(2, n):
        if prime[i] == 1:
            print(i, end=' ')


n = 200
start = time.time()
count_prime(n)
end = time.time()
print(end - start)

start = time.time()
sieve_of_Eratosthens(n)
end = time.time()
print(end - start)
