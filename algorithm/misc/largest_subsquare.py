"""
Given a matrix of '0' or 'X', found the largest subsquare surrounded with 'X'.
"""


def largest_subsquare(matrix):
    n = len(matrix[0])
    ver = [[0 for col in range(n)] for row in range(n)]
    hor = [[0 for col in range(n)] for row in range(n)]
    ver[0][0] = hor[0][0] = int(matrix[0][0] == 'X')
    # init ver and hor matrix
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'O':
                ver[i][j] = 0
                hor[i][j] = 0
            else:
                hor[i][j] = 1 if j == 0 else hor[i][j - 1] + 1
                ver[i][j] = 1 if i == 0 else ver[i - 1][j] + 1
    m = 0
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            small = min(ver[i][j], hor[i][j])
            while small > m:
                if ver[i][j - small + 1] >= small or hor[i - small + 1][j] >= small:
                    m = small
                    break
                small -= 1
    return m


matrix = [['X', 'O', 'X', 'X', 'X', 'X'],
          ['X', 'O', 'X', 'X', 'O', 'X'],
          ['X', 'X', 'X', 'O', 'O', 'X'],
          ['O', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'O', 'X', 'O'],
          ['O', 'O', 'X', 'O', 'O', 'O'],
          ]
print(largest_subsquare(matrix))
