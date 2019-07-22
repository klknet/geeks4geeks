"""
Check divisibility by 7.
Let b be the last digit of a number n and a be the number we get when we split off b.
The representation of the number may also be multiplied by any relatively prime to the divisor without changing its divisibility,
After observing 7 divides 21, we can perform following:
10*a + b
after multiplying by 2, this becomes
20*a + 2*b
and then
21*a - a + 2*b
Eliminating multiple of 21 gives
-a + 2*b
and multiplying by -1 gives
2*b -a
"""


def divisible(n):
    if n == 0 or n == 7:
        return True
    if 0<n<10:
        return False
    if n < 0:
        return divisible(-n)
    a = int(n / 10)
    b = n - a * 10
    diff = a - 2 * b
    return divisible(diff)


print(divisible(3717))
