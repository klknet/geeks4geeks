"""
How to check if an instance of 8 puzzle is solvable?
"""


def get_inv_count(arr, l, h):
    if l < h:
        m = l + ((h - l) >> 1)
        left_count = get_inv_count(arr, l, m)
        right_count = get_inv_count(arr, m + 1, h)
        left = arr[l:m + 1]
        right = arr[m + 1:h + 1]
        temp = []
        i = j = 0
        left_n, right_n = len(left), len(right)
        res = 0
        # do merge sort.
        while i < left_n and j < right_n:
            if left[i] > right[j]:
                if left[i] != 0 and right[j] != 0:
                    res += left_n - i
                temp.append(right[j])
                j += 1
            else:
                temp.append(left[i])
                i += 1
        while i < left_n:
            temp.append(left[i])
            i += 1
        while j < right_n:
            temp.append(right[j])
            j += 1
        for i in range(l, h + 1):
            arr[i] = temp.pop(0)
        return left_count + right_count + res
    return 0


def is_solvable(arr):
    c = get_inv_count(arr, 0, len(arr) - 1)
    print(c)
    return 'solvable' if c & 1 == 0 else 'unsolvable'


print(is_solvable([1, 8, 2, 0, 4, 3, 7, 6, 5]))
