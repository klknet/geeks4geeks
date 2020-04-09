import copy


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
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]
            # move right to top
            matrix[i][j] = matrix[j][n - i - 1]
            # move bottom to right
            matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
            # move left to bottom
            matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
            # move top to left
            matrix[n - j - 1][i] = tmp
    print_matrix(matrix)


def transpose_anticlockwise(matrix):
    """
    1)first compute the transpose matrix
    2)Then we reverse elements of every column
    :param matrix:
    :return:
    """
    n = len(matrix)
    # get transpose matrix
    for i in range(n):
        for j in range(i, n):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse every column.
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
    print_matrix(matrix)


def transpose_180(matrix):
    n = len(matrix)
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            print(matrix[i][j], end="  ")
        print()
    print()


def transpose_180_inplace(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], matrix[i][j]
    print_matrix(matrix)


def turn_image_90(matrix):
    """
    turn an image by 90-degree.
    :param matrix:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    tran = [[0 for col in range(m)] for row in range(n)]
    for i in range(m):
        for j in range(n):
            tran[j][m - 1 - i] = matrix[i][j]
    print_matrix(tran)


def rotate_k_element(matrix, k):
    """
    rotate a matrix of m*n by k in anti-clockwise.
    以螺旋方式复制环中元素到tmp数组，将前k个元素倒序添加到环尾。再将tmp数组以螺旋方式复制会原矩阵。
    :param matrix:
    :param k:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    tmp = []
    row = col = 0
    start = end = 0
    # copy ring elements to tmp
    while row < m and col < n:
        # copy first row to tmp
        for i in range(col, n):
            tmp.append(matrix[row][i])
            end += 1
        row += 1
        # copy last column to tmp
        for i in range(row, m):
            tmp.append(matrix[i][n - 1])
            end += 1
        n -= 1
        # copy last row to tmp
        for i in range(n - 1, col - 1, -1):
            tmp.append(matrix[m - 1][i])
            end += 1
        m -= 1
        # copy first column to tmp
        for i in range(m - 1, row - 1, -1):
            tmp.append(matrix[i][col])
            end += 1
        col += 1
        if end - start > k:
            reverse(tmp, start, start + k)
            reverse(tmp, start + k, end)
            reverse(tmp, start, end)
            start = end
    # copy tmp to matrix again.
    row = col = 0
    m, n = len(matrix), len(matrix[0])
    idx = 0
    while row < m and col < n:
        for i in range(col, n):
            matrix[row][i] = tmp[idx]
            idx += 1
        row += 1
        for i in range(row, m):
            matrix[i][n - 1] = tmp[idx]
            idx += 1
        n -= 1
        for i in range(n - 1, col - 1, -1):
            matrix[m - 1][i] = tmp[idx]
            idx += 1
        m -= 1
        for i in range(m - 1, row - 1, -1):
            matrix[i][col] = tmp[idx]
            idx += 1
        col += 1
    print_matrix(matrix)


def reverse(l, s, e):
    e -= 1
    while 0 <= s < e < len(l):
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(len(matrix), len(matrix[0]), copy.deepcopy(matrix))
    anti_clockwise(copy.deepcopy(matrix))
    transpose_anticlockwise(copy.deepcopy(matrix))
    transpose_180(copy.deepcopy(matrix))
    transpose_180_inplace(copy.deepcopy(matrix))
    image = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    turn_image_90(image)
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    rotate_k_element(copy.deepcopy(matrix), 3)
