"""
Program for array rotation.
"""


def left_rotation(arr, d):
    n = len(arr)
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i += 1
    while i < n:
        arr[i - d] = arr[i]
        i += 1
    for i in range(d):
        arr[n - d + i] = temp[i]


def left_rotation1(arr, d):
    """
    Using greatest common divisor.
    :param arr:
    :param d:
    :return:
    """
    g = _gcd(len(arr), d)
    for i in range(g):
        j = i
        temp = arr[i]
        while 1:
            k = j + d
            if k >= (len(arr)):
                k -= len(arr)
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def left_rotation2(arr, d):
    a = arr[:d]
    b = arr[d:]
    arbr = a.reverse() + b.reverse()
    return arbr.reverse()


def _gcd(a, b):
    if b == 0:
        return a
    else:
        return _gcd(b, a % b)


arr = [1, 2, 3, 4, 5, 6, 7]
left_rotation(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]
left_rotation1(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]
left_rotation1(arr, 2)
print(arr)
