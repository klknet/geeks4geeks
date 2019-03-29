"""
Parenthesization Problem
Given a boolean expression and operators between them. Count the number of ways we can parenthesize the expression so
that the value of the expression evaluates to true.

"""


def count_number(express, operator):
    n = len(express)
    # t[i][j] represents the number of ways to parenthesize the symbols between i and j(both inclusive) so that the
    # subexpression between i and j evaluates to true.
    t = [[0 for i in range(n)] for j in range(n)]
    # t[i][j] represents the number of ways to parenthesize the symboles between i and j (both inclusive) so that the
    # subexpression evaluates to false.
    f = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        t[i][i] = 1 if express[i] == 'T' else 0
        f[i][i] = 0 if express[i] == 'T' else 1
    for L in range(1, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                tik = t[i][k] + f[i][k]
                tkj = t[k + 1][j] + f[k + 1][j]
                if operator[k] == '&':
                    t[i][j] += t[i][k] * t[k + 1][j]
                    f[i][j] += (tik*tkj - t[i][k] * t[k + 1][j])
                elif operator[k] == '|':
                    t[i][j] += (tik*tkj - f[i][k] * f[k + 1][j])
                    f[i][j] += f[i][k] * f[k + 1][j]
                else:
                    t[i][j] += (t[i][k] * f[k + 1][j] + f[i][k] * t[k + 1][j])
                    f[i][j] += (t[i][k] * t[k + 1][j] + f[i][k] * f[k + 1][j])
    return t[0][n - 1]


e = "TTFT"
o = "|&^"
print(count_number(e, o))
