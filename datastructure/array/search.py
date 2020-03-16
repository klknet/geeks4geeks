def sum_pair_as_x(arr, x):
    """
    Given an array A[] and a number x, check for pair in A[] with sum as x.
    :param arr:
    :param x:
    :return:
    """
    arr.sort()
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == x:
            print(arr[i], arr[j])
            return True
        elif s > x:
            j -= 1
        elif s < x:
            i += 1
    return False


def pair_sum_as_x_hash(arr, x):
    t = set()
    for i in arr:
        if x - i in t:
            print(i, x - i)
            return True
        else:
            t.add(i)
    return False


def search_in_step_arr(arr, step, x):
    """
    Search in an array where adjacent diff by at most k.
    :param arr:
    :param step:
    :param x:
    :return:
    """
    i = 0
    while i < len(arr):
        if arr[i] == x:
            return i
        i += max(1, abs(x - arr[i]) // step)
    return -1


def find_common_ele(a1, a2, a3):
    """
    Find common elements in three common sorted arrays.
    :param a1:
    :param a2:
    :param a3:
    :return:
    """
    i = j = k = 0
    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] == a2[j] == a3[k]:
            print(a1[i], end=' ')
            i += 1
            j += 1
            k += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j] < a3[k]:
            j += 1
        else:
            k += 1


def find_repetitive_ele(arr):
    """
    Find the only repetitive element between 1 and n-1.
    Using sum, first compute sum of 1 to n-1 say s1, than compute sum of arr say s2,
    the result is s2-s1.
    :param arr:
    :return:
    """
    n = len(arr)
    s1 = (n-1)*n//2
    sw = sum(arr)
    return sw-s1


def find_repetitive_ele_xor(arr):
    """
    Find the only repetitive element between 1 and n-1.
    Using xor, base the fact x^x=0, x^y=y^x.
    so we can xor the arr with 1 to n-1, the result is answer.
    :param arr:
    :return:
    """
    res = 0
    for i in range(len(arr)):
        res ^= arr[i]^i
    return res


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8]
    x = 16
    print("have pair of sum equals to x", sum_pair_as_x(arr, x))
    print("have pair of sum equals to x", pair_sum_as_x_hash(arr, x))
    arr = [2, 4, 5, 7, 7, 6]
    print("element at index", search_in_step_arr(arr, 2, 7))
    a1 = [1, 5, 10, 20, 40, 80]
    a2 = [6, 7, 20, 80, 100]
    a3 = [3, 4, 15, 20, 30, 70, 80, 120]
    find_common_ele(a1, a2, a3)
    arr = [1, 5, 1, 2, 3, 4]
    arr = [1, 3, 2, 3, 4]
    print('Repetitive element is', find_repetitive_ele(arr))
    print('Repetitive element is', find_repetitive_ele_xor(arr))
