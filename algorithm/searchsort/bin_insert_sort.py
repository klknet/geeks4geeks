# Binary search in insertion sort


def binary_search(arr, l, r, x):
    while True:
        if r <= l:
            if arr[l] > x:
                return l
            else:
                return l + 1
        m = l + (r - l) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        v = arr[i]
        j = binary_search(arr, 0, i - 1, v)
        arr = arr[:j] + [v] + arr[j:i] + arr[i + 1:]
    return arr


if __name__ == '__main__':
    arr = [10, 6, 9, 2, 19, 23, 4, 8]
    print(insertion_sort(arr))
    print(arr)
