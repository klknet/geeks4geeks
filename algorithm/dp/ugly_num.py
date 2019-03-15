"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. Given a number n, the task is to find the n'th ugly
number.
Method 1
Loop for all positive integers util ugly number count is smaller than n, if an integer is ugly than increment ugly number
count.
To check if a number is ugly, divide the number by greatest divisible powers of 2, 3 and 5, if the number becomes 1 then
it is an ugly number otherwise not.

"""


def ugly_number_dp(n):
    t = [0] * n
    t[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        t[i] = min(t[i2] * 2, t[i3] * 3, t[i5] * 5)
        if t[i] == t[i2] * 2:
            i2 += 1
        if t[i] == t[i3] * 3:
            i3 += 1
        if t[i] == t[i5] * 5:
            i5 += 1
    return t[n - 1]


def ugly_number(n):
    count = 1
    i = 1
    while count < n:
        i += 1
        if _is_ugly(i):
            count += 1
    return i


def _is_ugly(no):
    no = _max_divide(no, 2)
    no = _max_divide(no, 3)
    no = _max_divide(no, 5)
    return no == 1


def _max_divide(a, b):
    while a % b == 0:
        a = a / b
    return a


n=100
print(ugly_number(n))
print(ugly_number_dp(n))
