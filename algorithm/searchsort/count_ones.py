# Count 1's in binary array
def count_ones(arr):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        m = l + (r - l) // 2
        if (arr[m] == 1) and (m == r or arr[m + 1] == 0):
            return m + 1
        elif arr[m] == 0:
            r = m - 1
        elif arr[m] == 1:
            l = m + 1
    return 0


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1, 0, 0, 0]
    arr = [1]
    print(count_ones(arr))
