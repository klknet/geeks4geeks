"""
Double the first element and move zero to end.
"""
import functools


def double_and_move(arr):
    """
    Double the first element equals to next element and move zeros to end.
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        if arr[i + 1] != 0 and arr[i] == arr[i + 1]:
            arr[i] <<= 1
            arr[i + 1] = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr


def reorder_index(arr, idx):
    """
    Reorder an array according to given indexes.
    :param arr:
    :param idx:
    :return:
    """
    i = 0
    while i < len(arr):
        if i != idx[i]:
            i1 = i
            i2 = idx[i]
            arr[i1], arr[i2] = arr[i2], arr[i1]
            idx[i1], idx[i2] = idx[i2], idx[i1]
        else:
            i += 1
    return arr, idx


def rearrange_pos_neg(arr):
    """
    Rearrange positive and negative numbers with constants extra space.
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        if arr[i] >= 0:
            continue
        j = i
        temp = arr[i]
        while j > 0:
            if arr[j - 1] > 0:
                arr[j] = arr[j - 1]
                j -= 1
            else:
                break
        arr[j] = temp
    return arr


def rearrange_pos_neg1(arr):
    """
    Using merge sort in place sort.
    :param arr:
    :return:
    """
    merge_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort(arr, l, r):
    if l < r:
        m = int((l + r) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, r, m)


def merge(arr, l, r, m):
    i, j = l, m + 1
    while i <= m and arr[i] < 0:
        i += 1
    while j <= r and arr[j] < 0:
        j += 1
    reverse(arr, i, m)
    reverse(arr, m + 1, j - 1)
    reverse(arr, i, j - 1)


def reverse(arr, s, e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1


def arrange_biggest_num(arr):
    """
    Arrange given numbers to form the biggest number.
    :param arr:
    :return:
    """
    arr.sort(key=functools.cmp_to_key(my_cmp), reverse=True)
    res = ''
    for i in arr:
        res += str(i)
    return res


def my_cmp(x, y):
    if x == y:
        return 0
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return 1
    return -1


def arrange_i_j(arr):
    """
    Rearrange an array such thant arr[j] = i if arr[i] = j.
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        arr[i] += 1
    for i in range(len(arr)):
        if arr[i] > 0:
            swap_i_j(arr, i, arr[i])
    for i in range(len(arr)):
        arr[i] = -arr[i] - 1
    return arr


def swap_i_j(arr, idx, val):
    next_idx = val - 1
    if arr[next_idx] > 0:
        tmp = arr[next_idx]
        arr[next_idx] = -idx - 1
        swap_i_j(arr, next_idx, tmp)


def rearrange_wave(arr):
    arr.sort(reverse=False)
    for i in range(1, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def rearrange_wave1(arr):
    for i in range(len(arr)-1):
        if i & 1 == 0:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print("Double the first element equals to next element and move zeros to end.\n",
      double_and_move([0, 2, 2, 2, 0, 6, 6, 0, 0, 8]))
print("Reorder an array according to given indexes.\n", reorder_index([50, 40, 70, 60, 90], [3, 0, 4, 1, 2]))
print("arrange positive and negative numbers.\n", rearrange_pos_neg([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print("arrange positive and negative numbers.\n", rearrange_pos_neg1([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print("Form the biggest number.\n", arrange_biggest_num([54, 546, 548, 60]))
print("swap arr[i] = j if arr[j] = i.\n", arrange_i_j([1, 3, 0, 2]))
print("swap arr[i] = j if arr[j] = i.\n", arrange_i_j([2, 0, 1, 4, 5, 3]))
print("rearrange arr in wave order.\n", rearrange_wave([6, 4, 2, 1, 8, 3, 10]))
print("rearrange arr in wave order.\n", rearrange_wave1([6, 4, 2, 1, 8, 3]))
