"""
Median of two sorted arrays of same size.
1)Calculate the medians m1 and m2 of the input arrays arr1 and arr2 respectively.
2)If m1 and m2 are both equal, then we are done.
    :return m1 or m2
3)If m1 is greater than m2, then median is present in one of the below two subarrays.
    a)From first element of arr1 to m1(arr[0..._n/2_])
    b)From m2 to last element of arr2(arr[_n/2_...n])
4)Repeat the above process util size of both the subarrays become 2.
5)If size of the two arrayss is 2 then use below formula to get the median.
    Median = (max(arr1[0], arr2[0]), min(arr1[1], arr2[1]))/2
"""


def mid_of_arr(arr1, arr2, n):
    if n == 0:
        return -1
    elif n == 1:
        return (arr1[0] + arr2[0]) // 2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) // 2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
        if m1 > m2:
            if n & 1 == 0:
                return mid_of_arr(arr1[:int(n / 2) + 1], arr2[int(n / 2) - 1:], n // 2 + 1)
            else:
                return mid_of_arr(arr1[:int(n / 2) + 1], arr2[int(n / 2):], int(n / 2) + 1)
        else:
            if n & 1 == 0:
                return mid_of_arr(arr1[int(n / 2) - 1:], arr2[:int(n / 2 + 1)], n // 2 + 1)
            else:
                return mid_of_arr(arr1[int(n / 2):], arr2[:int(n / 2) + 1], int(n / 2) + 1)


def median(arr, n):
    if n & 1 == 0:
        return (arr[int(n / 2)]+arr[int(n / 2) - 1]) / 2
    return arr[int(n / 2)]


a1 = [1, 2, 3, 6]
a2 = [4, 6, 8, 10]
print(mid_of_arr(a1, a2, len(a1)))
a1 = [1, 12, 15, 26, 38]
a2 = [2, 13, 17, 30, 45]
print(mid_of_arr(a1, a2, len(a1)))
