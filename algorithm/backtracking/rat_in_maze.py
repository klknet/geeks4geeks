"""
Rat in a maze.
"""

sol = []
n = 4
xMove = [1, 0]
yMove = [0, 1]


def find_path_util(matrix, x, y):
    if x == n - 1 and y == n - 1:
        return True
    for k in range(2):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if next_x < n and next_y < n and matrix[next_x][next_y] == 1:
            sol.append((next_x, next_y))
            if find_path_util(matrix, next_x, next_y):
                return True
            else:
                sol.pop()
    return False


def find_path(matrix):
    sol.append((0,0))
    if find_path_util(matrix, 0, 0):
        for i in range(len(sol)):
            print(sol[i])


m = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
find_path(m)