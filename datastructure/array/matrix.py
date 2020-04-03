def rotate_matrix(m, n, matrix):
    """
    Clockwise rotate elements in it.
    One by one rotate all rings of elements, starting from the outermost. To rotate a ring, we need to do following
    1)Move elements of top row
    2)Move elements of last column
    3)Move elements of bottom row
    4)Move elements of first column
    :param m:
    :param n:
    :param matrix:
    :return:
    """
    row = col = 0
    while row < m and col < n:
        if row + 1 == m or col + 1 == n:
            break
        prev = matrix[row + 1][col]
        # move elements of top row
        for i in range(col, n):
            matrix[row][i], prev = prev, matrix[row][i]
        row += 1
        # move elements of last col
        for i in range(row, m):
            matrix[i][n - 1], prev = prev, matrix[i][n - 1]
        n -= 1
        # move elements of last row
        for i in range(n - 1, col - 1, -1):
            matrix[m - 1][i], prev = prev, matrix[m - 1][i]
        m -= 1
        # move elements of first col
        for i in range(m - 1, row - 1, -1):
            matrix[i][col], prev = prev, matrix[i][col]
        col += 1
    print_matrix(matrix)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='  ')
        print()
    print()


def anti_clockwise(matrix):
    """
    rotate a matrix 90 degrees in anti-clockwise
    :param matrix:
    :return:
    """
    n = len(matrix)
    # have n/2 cycles.
    for i in range(n // 2):
        for j in range(i, n - i -1):
            tmp = matrix[i][j]
            # move right to top
            matrix[i][j] = matrix[j][n - i - 1]
            # move bottom to right
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            # move left to bottom
            matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
            # move top to left
            matrix[n-j-1][i] = tmp
    print_matrix(matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(len(matrix), len(matrix[0]), matrix)
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    anti_clockwise(matrix)
