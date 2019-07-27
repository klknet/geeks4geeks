"""
Print pascal triangle.
"""


def pascal_triangle(n):
    # tab = [[1 for col in range(n)] for row in range(n)]
    tab = [1] * n
    for i in range(n):
        t = [1] * (i + 1)
        for j in range(i + 1):
            if j == 0 or j == i:
                t[j] = 1
            else:
                t[j] = tab[j - 1] + tab[j]
        print(t)
        tab = t


def pascal(n):
    for i in range(1, n + 1):
        prev = 1
        for j in range(1, i + 1):
            print(prev, end=" ")
            prev = prev * (i - j) // j
        print()


n = 7
pascal_triangle(n)
pascal(n)
