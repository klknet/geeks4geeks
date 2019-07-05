"""
A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, in a square, such that the n numbers
in all rows, all columns and both diagonals sum to the same constant. A magic square contains the integers from 1 to n^2.

The constant sum in every row, column and diagonal is called the magic constant or magic sum, M. The magic constant of a
normal magic square depends only on n and has following value.
M = n(n^2+1)/2
In any magic square, the first number i.e 1 is stored at position (n/2, n-1). Let this position be (i,j). The next position
is stored at (i-1,j+1) where we can consider all row & column as circular array i.e they wrap around.
If the magic square already contains a number at the calculated position, calculated column position will be decremented by
2, and calculated row position will be incremented by 1.
"""


def magic_square(n):
    M = n * (n ** 2 + 1) // 2
    res = [[0 for i in range(n)] for j in range(n)]
    i, j = n // 2, n - 1
    res[i][j] = 1
    for k in range(2, n * n + 1, 1):
        i = i - 1 if i > 0 else n - 1
        j = (j + 1) % n
        if res[i][j] == 0:
            res[i][j] = k
        else:
            i = (i + 1) % n
            j = j - 2 if j > 1 else n + j - 2
            res[i][j] = k
    for i in range(n):
        print(res[i])


magic_square(8)
