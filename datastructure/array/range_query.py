"""
Range Queries.
"""
import math

lookup = None
lookup1 = None
frequency = None


def sparse_table(arr, l, r):
    global lookup
    sqrt = math.floor(math.sqrt(len(arr)))
    if lookup is None:
        lookup = [[0 for i in range(sqrt)] for j in range(len(arr))]
        for i in range(len(arr)):
            lookup[i][0] = arr[i]
        for j in range(1, sqrt):
            i = 0
            while i + (1 << j) - 1 < len(arr):
                if lookup[i][j - 1] < lookup[i + (1 << (j - 1))][j - 1]:
                    lookup[i][j] = lookup[i][j - 1]
                else:
                    lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
                i += 1
    j = math.floor(math.log(r - l + 1, 2))
    if lookup[l][j] < lookup[r - (1 << j) + 1][j]:
        return lookup[l][j]
    return lookup[r - (1 << j) + 1][j]


def sparse_table_sum(arr, l, r):
    global lookup1
    k = 16
    if lookup1 is None:
        lookup1 = [[0 for i in range(k)] for j in range(len(arr))]
        n = len(arr)
        for i in range(n):
            lookup1[i][0] = arr[i]
        for j in range(1, k + 1):
            i = 0
            while i + (1 << j) - 1 < n:
                lookup1[i][j] = lookup1[i][j - 1] + lookup1[i + (1 << (j - 1))][j - 1]
                i += 1
    res = 0
    for i in range(k, -1, -1):
        if l + (1 << i) - 1 <= r:
            res += lookup1[l][i]
            l += (1 << i)
    return res


def range_frequencies(arr, l, r, ele):
    global frequency
    if frequency is None:
        frequency = {}
        for i in range(len(arr)):
            if arr[i] in frequency:
                frequency[arr[i]].append(i)
            else:
                frequency[arr[i]] = [i]
    ran = frequency[ele]
    return binary_search_greater(ran, 0, len(ran) - 1, r) - binary_search(ran, 0, len(ran) - 1, l)


def binary_search(arr, l, r, e):
    if arr[l] > e:
        return l
    if l <= r:
        m = int((l + r) / 2)
        if m > l and arr[m - 1] < e <= arr[m]:
            return m
        if m == l and arr[m] >= e:
            return m
        if arr[m] < e:
            return binary_search(arr, m + 1, r, e)
        else:
            return binary_search(arr, l, m, e)
    return -1


def binary_search_greater(arr, l, r, e):
    if arr[r] <= e:
        return r+1
    if l <= r:
        m = int((l + r) / 2)
        if m > l and arr[m - 1] <= e < arr[m]:
            return m
        if m == l and arr[m] > e:
            return m
        if arr[m] <= e:
            return binary_search_greater(arr, m + 1, r, e)
        else:
            return binary_search_greater(arr, l, m, e)
    return -1


if __name__ == '__main__':
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    print(sparse_table(arr, 0, 4))
    print(sparse_table(arr, 4, 7))
    print(sparse_table(arr, 7, 8))

    arr = [3, 7, 2, 5, 8, 9]
    assert sparse_table_sum(arr, 0, 5) == 34
    assert sparse_table_sum(arr, 3, 5) == 22
    assert sparse_table_sum(arr, 2, 4) == 15

    arr = [2, 8, 6, 9, 8, 6, 8, 2, 11]
    # arr = [2, 3, 5, 8]
    # print(binary_search(arr, 0, len(arr) - 1, 9))
    assert range_frequencies(arr, 0, 5, 2) == 1
    assert range_frequencies(arr, 3, 8, 8) == 2
