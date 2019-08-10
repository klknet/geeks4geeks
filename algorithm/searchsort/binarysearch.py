def binary_search_recur(arr, x, l, r):
    if l > r:
        return -1
    mid = l + ((r - l) >> 1)  # 取中位数 防止int溢出
    if arr[mid] > x:
        # mid不用取，忘前挪一位
        return binary_search_recur(arr, x, l, mid - 1)
    elif arr[mid] < x:
        # mid忘后挪一位
        return binary_search_recur(arr, x, mid + 1, r)
    else:
        return mid


def binary_search_itr(arr, x, l, r):
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            return mid
    return -1


def binary_search(arr, x):
    """
    Search in an almost sorted array
    :param arr:
    :param x:
    :return:
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + ((r - l) >> 1)
        if arr[m] == x:
            return m
        if m > l and arr[m - 1] == x:
            return m - 1
        if m < r and arr[m + 1] == x:
            return m + 1
        if arr[m] < x:
            l = m + 2
        else:
            r = m - 2
    return -1


def floor(arr, n):
    l, h = 0, len(arr) - 1
    while l < h:
        m = l + ((h - l) >> 1)
        if arr[m] < n:
            l = m + 1
        else:
            h = m
    if l == len(arr) - 1 and arr[l] < n:
        return None
    return arr[l]


def ceil(arr, n):
    l, h = 0, len(arr) - 1
    while l < h:
        m = l + ((h - l) >> 1) + 1
        if arr[m] > n:
            h = m - 1
        else:
            l = m
    if l == 0 and arr[l] > n:
        return None
    return arr[l]


if __name__ == '__main__':
    arr = list(range(30))
    for i in range(-3, 33):
        # print(binary_search_recur(arr, i, 0, len(arr) - 1), end=" ")
        # print(binary_search_itr(arr, i, 0, len(arr) - 1), end=" ")
        pass
    arr = [3, 2, 10, 4, 40]
    # print(binary_search(arr, -3))

    arr = [1, 4, 7, 10, 13, 16, 19, 22]
    print('floor', floor(arr, 23))
    print('ceil', ceil(arr, 1.2))
