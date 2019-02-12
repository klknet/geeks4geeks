# Find the closest pair from two sorted arrays


import sys


def print_closest(a1, a2, x):
    """
    1) Initialize a variable diff as infinite(Diff is used to store the difference between pair and x), We need to find
       the minimum diff.
    2) Initialize two index variables l and r in the given sorted array.
        (a) Initialize first to the leftmost index in a1: l=0
        (b) Initialize second to the rightmost index in a2: r=n-1
    3) Loop while l<m and r>=0
        (a) If a1[l]+a2[r]-x < diff:
                then update diff and result
        (b) If a1[l]+a2[r] < sum then l++
        (c) Else then r--
    4) Print the result.
    :param a1:
    :param a2:
    :param x:
    :return:
    """
    m, n = len(a1), len(a2)
    l, r = 0, n - 1
    diff = sys.maxsize
    while l < m and r >= 0:
        if abs(a1[l] + a2[r] - x) < diff:
            diff = abs(a1[l] + a2[r] - x)
            res_l, res_r = l, r
        if a1[l] + a2[r] > x:
            r -= 1
        else:
            l += 1
    print('The closest pair is', a1[res_l], a2[res_r])


# Find the closest element to x
def closest_pair(a1, a2, x):
    cp1 = cross_point(a1, x)
    cp2 = cross_point(a2, x)
    return a1[cp1], a2[cp2]


def cross_point(arr, x):
    n = len(arr)
    l, r = 0, n - 1
    if arr[l] >= x:
        return l
    if arr[r] <= x:
        return r
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] <= x < arr[m + 1]:
            return m if arr[m + 1] - x >= x - arr[m] else m + 1
        if arr[m] > x:
            r = m - 1
        else:
            l = m + 1


def single_close_pair(arr, x):
    """
    Given a sorted array and a number x, find the pair in the array whose sum is closest to x
    :param arr:
    :param x:
    :return:
    """
    n = len(arr)
    l, r = 0, n-1
    diff = sys.maxsize
    while l<r:
        if abs(arr[l]+arr[r]-x) < diff:
            diff = abs(arr[l]+arr[r]-x)
            f = l
            s = r
        if arr[l]+arr[r]<x:
            l += 1
        else:
            r -= 1
    return arr[f], arr[s]


if __name__ == '__main__':
    a1 = [2, 5, 7, 19, 34, 45]
    a2 = [-9, -8, 13, 23, 31]
    # print(closest_pair(a1, a2, 0))
    print_closest(a1, a2, -1)
    print(single_close_pair(a1, 99))
    print(single_close_pair(a2, 9))
