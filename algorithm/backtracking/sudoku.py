"""
Sudoku.
Given a partially filled 9*9 2D  array 'grid[9][9]', the goal is to assign digits(from 1 to 9) to empty cells so that
every row, column and subgrid of size 3*3 contains exactly one instance of digits from 1 to 9.
"""

N = 9
unassign = 0


def sudoku(matrix):
    pos = [-1, -1]
    if not find_unassigned(matrix, pos):
        return True
    for i in range(1, 10):
        if isSafe(matrix, pos, i):
            matrix[pos[0]][pos[1]] = i
            if sudoku(matrix):
                return True
            matrix[pos[0]][pos[1]] = unassign
    return False


def isSafe(matrix, pos, num):
    return not (useInRow(matrix, pos, num) or useInCol(matrix, pos, num) or useInBox(matrix, pos, num))


def useInRow(matrix, pos, num):
    for i in range(N):
        if matrix[pos[0]][i] == num:
            return True
    return False


def useInCol(matrix, pos, num):
    for i in range(N):
        if matrix[i][pos[1]] == num:
            return True
    return False


def useInBox(matrix, pos, num):
    row = pos[0] // 3
    col = pos[1] // 3
    for i in range(3):
        for j in range(3):
            if matrix[row * 3 + i][col * 3 + j] == num:
                return True
    return False


def find_unassigned(matrix, pos):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == unassign:
                pos[0], pos[1] = i, j
                return True
    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
if sudoku(grid):
    for i in range(N):
        print(grid[i])
else:
    print('no solution')
