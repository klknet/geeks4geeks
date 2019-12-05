"""
Given a sorted and rotated array, find if there is a pair with a given sum.
"""


def find_pos(arr, l, r, s):
    while l != r:
        cur = arr[l] + arr[r]
        if cur == s:
            return l, r
        elif cur > s:
            # move to the lower sum side.
            r = (r - 1 + len(arr)) % len(arr)
        elif cur < s:
            # move to the higher sum side.
            l = (l + 1) % len(arr)
    return None


def pivot_index(arr, low, high):
    if low == high:
        return low
    m = int((low + high) / 2)
    if m < high and arr[m] > arr[m + 1]:
        return m
    if m > low and arr[m] < arr[m - 1]:
        return m - 1
    return pivot_index(arr, m + 1, high)


def pair(arr, s):
    p = pivot_index(arr, 0, len(arr) - 1)
    l, r = (p + 1) % len(arr), p
    return find_pos(arr, l, r, s)


arr = [11, 15, 6, 8, 9, 10]
print(pair(arr, 16))
