"""
In mathematical terms, the sequence Fn of fibonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2
with seed values
F0 = 0, F1 = 1
"""


# recursive implementation
def fib_recur(n):
    if n < 2:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


# dynamic programming
def fib_dp(n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


# optimal dynamic programming
def fib_dp_opt(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        s = a + b
        a = b
        b = s
    return s


# using matrix multiplication
# [(1,1),(1,0)]^n = [(Fn+1, Fn),(Fn, Fn-1)]
def fib_matrix(n):
    a, b, c, d = 1, 1, 1, 0
    # n power of [(1,1),(1,0)]
    for i in range(2, n + 1):
        a, b, c, d = a + b, a, c + d, c
    return b


# using binary search of pow(M, N) of matrix multiplication
def fib_matrix_bs(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    if n & 1 == 1:
        h = fib_matrix_bs((n - 1) // 2)
        h = multiply(h, h)
        return multiply(h, [[1, 1], [1, 0]])
    else:
        h = fib_matrix_bs(n // 2)
        return multiply(h, h)


def multiply(m, n):
    return [[m[0][0] * n[0][0] + m[0][1] * n[1][0], m[0][0] * n[0][1] + m[0][1] * n[1][1]],
            [m[1][0] * n[0][0] + m[1][1] * n[1][0], m[1][0] * n[0][1] + m[1][1] * n[1][1]]]


n = 10
print(fib_recur(n))
print(fib_dp(n))
print(fib_dp_opt(n))
print(fib_matrix(n))
print(fib_matrix_bs(n)[0][1])
