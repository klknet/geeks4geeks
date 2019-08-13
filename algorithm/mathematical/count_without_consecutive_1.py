"""
Count number of binary strings without consecutive 1's.
"""


def count_consecutive(n):
    prev_prev = 1
    prev = 2
    cur = 0
    for i in range(1, n):
        cur = prev_prev + prev
        prev_prev = prev
        prev = cur
    return cur


def count(n):
    a = b = 1
    for i in range(1, n):
        a, b = a + b, a
    return a + b


def find_smallest(n):
    if n < 10:
        return n + 10
    res = []
    for i in range(9, 1, -1):
        while n % i == 0:
            n = int(n / i)
            res.append(i)
    if n > 10:
        return None
    res.reverse()
    return res


n = 5
print(count_consecutive(n))
print(count(n))
print(find_smallest(108))
