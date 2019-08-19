"""
Multiply two polynomials.
"""


def multiply(a, b):
    m, n = len(a), len(b)
    t = m + n - 1
    res = []
    for i in range(t):
        t = 0
        for j in range(i + 1):
            if j < m and i - j < n:
                t += a[j] * b[i - j]
        res.append(t)
    return res


def multiply1(a, b):
    m, n = len(a), len(b)
    poly = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            poly[i + j] += a[i] * b[j]
    return poly


print(multiply([5, 0, 10, 6], [1, 2, 4]))
print(multiply1([5, 0, 10, 6], [1, 2, 4]))
