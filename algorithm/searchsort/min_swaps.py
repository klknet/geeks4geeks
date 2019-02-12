# Minimum adjacent swaps to move maximum and minimum to corners

def min_swaps(arr):
    minn, maxx, l, r, n = arr[0], arr[0], 0, 0, len(arr)
    for i in range(n):
        if arr[i] > maxx:
            maxx = arr[i]
            l = i
        if arr[i] <= minn:
            minn = arr[i]
            r = i
    if l <= r:
        print(l + n - 1 - r)
    else:
        print(l + n - 2 - r)


arr = [3, 1, 5, 3, 5, 5, 2]
min_swaps(arr)
