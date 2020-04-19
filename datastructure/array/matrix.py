import copy
import sys


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


def check_rows_circular_rotation(matrix):
    """
    Check if all rows of a matrix are circular rotations of each other.
    :param matrix:
    :return:
    """
    str_concat = "".join(map(lambda x: str(x), matrix[0])) * 2
    for i in range(len(matrix)):
        str_curr = "".join(map(lambda x: str(x), matrix[i]))
        if str_concat.find(str_curr) == -1:
            return False
    return True


def sort_matrix(matrix):
    """
    Sort the given matrix
    :param matrix:
    :return:
    """
    n = len(matrix)
    tmp = []
    for i in range(n):
        for j in range(n):
            tmp.append(matrix[i][j])
    tmp.sort()
    idx = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = tmp[idx]
            idx += 1
    print_matrix(matrix)


def find_row_with_max_1s(matrix):
    """
    Find the row with maximum number 1s.
    :param matrix:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    left_1_idx = first(matrix[0], 0, n - 1)
    j = left_1_idx
    if left_1_idx == -1:
        j = n - 1
    max_row_idx = 0
    for i in range(1, m):
        while j >= 0 and matrix[i][j] == 1:
            j -= 1
            max_row_idx = i
    return max_row_idx


def first(arr, low, high):
    """
    Find the first 1s.
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low <= high:
        mid = int((low + high) / 2)
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 1:
            return first(arr, low, mid - 1)
        elif arr[mid] == 0:
            return first(mid + 1, high)
    return -1


def multiply(M, N):
    m1, n1 = len(M), len(M[0])
    m2, n2 = len(N), len(N[0])
    if n1 != m2:
        print("Not possible")
        return
    c = [[0 for i in range(n2)] for j in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for z in range(n1):
                c[i][j] += M[i][z] * N[z][j]
    print_matrix(c)


def lower_triangular(matrix):
    """
    Lower triangular matrix.
    :param matrix:
    :return:
    """
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            if j > i:
                matrix[i][j] = 0
    print_matrix(matrix)


def upper_triangular(matrix):
    """
    Upper triangular matrix.
    :param matrix:
    :return:
    """
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            if j < i:
                matrix[i][j] = 0
    print_matrix(matrix)


def common_elements(matrix):
    """
    Find the common elements of every row.
    :param matrix:
    :return:
    """
    n = len(matrix)
    for i in range(n):
        matrix[i].sort()
    idx = [0] * n
    res = []
    while True:
        equal = True
        for i in range(1, n):
            if matrix[i][idx[i]] != matrix[i - 1][idx[i - 1]]:
                equal = False
                break
        if equal:
            res.append(matrix[0][idx[0]])
        min_val = sys.maxsize
        min_idx = 0
        for i in range(n):
            if matrix[i][idx[i]] < min_val:
                min_val = matrix[i][idx[i]]
                min_idx = i
        if idx[min_idx] + 1 == n:
            break
        else:
            idx[min_idx] += 1
    return res


def common_elements_1(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i].sort()
    idx = [0] * n
    res = []
    f = 0
    for i in range(n):
        present = True
        value = matrix[0][idx[0]]
        idx[0] += 1
        for j in range(1, n):
            while idx[j] < n and matrix[j][idx[j]] <= value:
                idx[j] += 1
            if matrix[j][idx[j] - 1] != value:
                present = False
            if idx[j] == n:
                f = 1
                # break
        if present:
            res.append(value)
        if f == 1:
            break
    return res


def common_elements_2(matrix):
    n = len(matrix)
    h = dict()
    for i in range(n):
        h[matrix[0][i]] = 1
    for i in range(1, n):
        tmp = dict()
        for j in range(n):
            tmp[matrix[i][j]] = 1
        for e in list(h):
            if e not in tmp:
                del h[e]
    return list(h)


def spiral_form(matrix):
    m, n = len(matrix), len(matrix[0])
    row = col = 0
    while row < m and col < n:
        # print first row
        for i in range(row, n):
            print(matrix[row][i], end='  ')
        row += 1
        # print last column
        for i in range(row, m):
            print(matrix[i][n - 1], end='  ')
        n -= 1
        # print last row
        if row < m:
            for i in range(n - 1, col - 1, -1):
                print(matrix[m - 1][i], end='  ')
            m -= 1
        # print first column
        if col < n:
            for i in range(m - 1, row - 1, -1):
                print(matrix[i][col], end='  ')
        col += 1
    print()


def shift_matrix_k(matrix, k):
    """
    Shift matrix elements row-wist by k.
    :param matrix:
    :param k:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        row = matrix[i]
        reverse(row, 0, k)
        reverse(row, k, n)
        reverse(row, 0, n)
    print_matrix(matrix)


def counter_clock_spiral_form(matrix):
    m, n = len(matrix), len(matrix[0])
    row = col = 0
    while row<m and col<n:
        # print first column
        for i in range(row, m):
            print(matrix[i][col], end='  ')
        col += 1
        # pring last row
        for i in range(col, n):
            print(matrix[m-1][i], end='  ')
        m -= 1
        # print last column
        if col<n:
            for i in range(m-1, row-1, -1):
                print(matrix[i][n-1], end='  ')
        n -= 1
        # print first row
        if row < m:
            for i in range(n-1, col-1, -1):
                print(matrix[row][i], end='  ')
        row += 1


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
    matrix = [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]
    print(check_rows_circular_rotation(matrix))
    matrix = [[5, 4, 7], [1, 3, 8], [2, 9, 6]]
    sort_matrix(matrix)
    matrix = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    print('maximum 1s row', find_row_with_max_1s(matrix))
    M = [[2, 4], [3, 4]]
    N = [[1, 2], [1, 3]]
    multiply(M, N)
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    lower_triangular(copy.deepcopy(matrix))
    upper_triangular(copy.deepcopy(matrix))
    matrix = [[2, 1, 4, 3], [1, 2, 3, 2], [3, 6, 2, 3], [5, 2, 5, 3]]
    print("common elements", common_elements(copy.deepcopy(matrix)))
    # matrix = [[3, 4, 5], [1, 2, 3], [1, 2, 4]]
    print("common elements", common_elements_1(copy.deepcopy(matrix)))
    print("common elements", common_elements_2(copy.deepcopy(matrix)))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
    spiral_form(matrix)
    shift_matrix_k(copy.deepcopy(matrix), 2)
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    counter_clock_spiral_form(matrix)
