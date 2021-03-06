import sys


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


def find_pos_of_inf_arr(arr, key):
    """
    Find position of an element in a sorted array of infinite numbers.
    :param arr:
    :param key:
    :return:
    """
    pos = find_position(arr, key)
    l, h = pos // 2, pos
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            h = m - 1
        else:
            l = m + 1
    return -1


def find_position(arr, key):
    h = 1
    while arr[h] < key:
        h = 2 * h
    return h


def find_repetitive_ele(arr):
    """
    Find the only repetitive element between 1 and n-1.
    Using sum, first compute sum of 1 to n-1 say s1, than compute sum of arr say s2,
    the result is s2-s1.
    :param arr:
    :return:
    """
    n = len(arr)
    s1 = (n - 1) * n // 2
    sw = sum(arr)
    return sw - s1


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
        res ^= arr[i] ^ i
    return res


def max_sum_arr(arrA, arrB):
    """
    Find the contiguous subarray sum which not include in another array.
    :param arrA:
    :param arrB:
    :return:
    """
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(arrA)):
        if in_arr(arrB, arrA[i]):
            max_ending_here = 0
            continue
        max_ending_here += arrA[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def in_arr(arr, x):
    for i in arr:
        if x == i:
            return True
    return False


def equal_prefix_suffix_sum(arr):
    """
    Find the maximum prefix sum which is also suffix sum for index i in arr.
    :param arr:
    :return:
    """
    s = sum(arr)
    prefix = 0
    m = -sys.maxsize
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == s:
            m = max(m, prefix)
        s -= arr[i]
    return m


def equilibrium(arr):
    """
    Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of
    elements at higher indexes.
    :param arr:
    :return:
    """
    s = sum(arr)
    low = 0
    for i in range(len(arr)):
        s -= arr[i]
        if low == s:
            return i
        low += arr[i]
    return -1


def leaders_in_array(arr):
    """
    An element is leader if it is greater than all the elements to its right side.
    :param arr:
    :return:
    """
    m = arr[-1]
    res = [m]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > m:
            m = arr[i]
            res.append(m)
    return res


def ceil_of_x(arr, x):
    """
    The ceiling of x is the smallest element in array greater than or equal to x.
    :param arr:
    :param x:
    :return:
    """
    if arr[-1] < x:
        return None
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return arr[l]


def floor_of_x(arr, x):
    """
    The floor of x is the greatest element in array smaller than or equal to x.
    :param arr:
    :param x:
    :return:
    """
    if arr[0] > x:
        return None
    l, h = 0, len(arr) - 1
    while l < h:
        m = (l + h) // 2
        if arr[m] > x:
            h = m
        else:
            l = m + 1
    if arr[l] <= x:
        return arr[l]
    return arr[l - 1]


def majority_element(arr):
    """
    Majority Element. A majority element in an array a[] of size n is an element that appears more than n/2 times.
    Using Moore's Voting Algorithm.
    Basic idea of the algorithm is that if we cancel out each occurrence of element e with all other elements that are
    different from e then e will exist till end if it is a majority element.
    :param arr:
    :return:
    """
    major = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[major]:
            count -= 1
        else:
            count += 1
        if count == 0:
            major = i
            count = 1
    half = len(arr) // 2 + 1
    count = 0
    for e in arr:
        if e == arr[major]:
            count += 1
    if count >= half:
        return arr[major]
    return None


def check_for_majority(arr, x):
    """
    Find if a given integer appears more than n/2 times in a sorted array of n size.
    :param arr:
    :param x:
    :return:
    """
    idx = first_occurrence(arr, x)
    if idx == -1:
        return False
    n = idx + len(arr) // 2
    return n < len(arr) and arr[n] == x


def first_occurrence(arr, x):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if m == 0 and arr[m] == x:
            return m
        elif arr[m] == x and arr[m - 1] < x:
            return m
        if arr[m] >= x:
            r = m
        else:
            l = m + 1
    return -1


def find_peak(arr):
    """
    Find a peak element. An array element is peak if it is NOT SMALLER THAN its neighbors.
    :param arr:
    :return:
    """
    return find_peak_util(arr, 0, len(arr) - 1)


def find_peak_util(arr, l, r):
    m = (l + r) // 2
    if (m == 0 or arr[m] >= arr[m - 1]) and \
            (m == len(arr) - 1 or arr[m] >= arr[m + 1]):
        return m
    elif m > 0 and arr[m] <= arr[m - 1]:
        return find_peak_util(arr, l, m - 1)
    else:
        return find_peak_util(arr, m + 1, r)


def find_fixed_point(arr):
    """
    Find a fixed point in an array.
    Fixed point in an array is an index i such that arr[i] equal to i.
    :param arr:
    :return:
    """
    l, r = 0, len(arr)
    while l <= r:
        m = (l + r) // 2
        if arr[m] == m:
            return m
        elif arr[m] < m:
            l = m + 1
        else:
            r = m - 1
    return -1


def subarray_sum_equal_to_x(arr, x):
    """
    Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
    :param arr:
    :param x:
    :return:
    """
    curr_sum = arr[0]
    start = 0
    for i in range(1, len(arr) + 1):
        while curr_sum > x and start <= i - 1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == x:
            print("find subarray, start at %s end at %s" % (start, i - 1))
            return
        if i < len(arr):
            curr_sum += arr[i]
    print("No solution")


def max_triplet_sum(arr):
    """
    Maximum triplet sum in array.
    :param arr:
    :return:
    """
    first = second = third = -sys.maxsize
    for e in arr:
        if e > first:
            third = second
            second = first
            first = e
        elif e > second:
            third = second
            second = e
        elif e > third:
            third = e
    return first + second + third


def smallest_diff_triplet(a1, a2, a3):
    """
    smallest difference triplet from three arrays.
    :param a1:
    :param a2:
    :param a3:
    :return:
    """
    n = len(a1)
    a1.sort()
    a2.sort()
    a3.sort()
    f = s = t = 0
    diff = sys.maxsize
    small = mid = big = 0
    while f < n and s < n and t < n:
        max_v = max(a1[f], a2[s], a3[t])
        min_v = min(a1[f], a2[s], a3[t])
        sum_v = sum([a1[f], a2[s], a3[t]])
        if a1[f] == min_v:
            f += 1
        elif a2[s] == min_v:
            s += 1
        else:
            t += 1
        if diff > max_v - min_v:
            small = min_v
            big = max_v
            mid = sum_v - max_v - min_v
            diff = max_v - min_v
    return small, mid, big


def triplet_sum(arr, x):
    """
    Find a triplet that sum to a given value.
    :param arr:
    :param x:
    :return:
    """
    arr.sort()
    f = 0
    for f in range(len(arr) - 2):
        l = f + 1
        r = len(arr) - 1
        while l < r:
            s = arr[l] + arr[r] + arr[f]
            if s == x:
                return arr[f], arr[l], arr[r]
            elif s < x:
                l += 1
            else:
                r -= 1
    return None


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
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    print("\nPosition of an element in a sorted of infinite numbers", find_pos_of_inf_arr(arr, 10))
    arr = [1, 5, 1, 2, 3, 4]
    arr = [1, 3, 2, 3, 4]
    print('Repetitive element is', find_repetitive_ele(arr))
    print('Repetitive element is', find_repetitive_ele_xor(arr))
    arrA = [1, 7, -10, 6, 2]
    arrA = [3, 4, 5, -4, 6]
    arrB = [5, 6, 7, 1]
    arrB = [1, 8, 5]
    print("Maximum contiguous subarray sum is", max_sum_arr(arrA, arrB))
    arr = [-2, 5, 3, 1, 2, 6, -4, 2]
    print("Maximum prefix sum equals suffix sum", equal_prefix_suffix_sum(arr))
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print("Equilibrium index is", equilibrium(arr))
    arr = [16, 17, 4, 3, 5, 2]
    print("Leaders in array", leaders_in_array(arr))
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 19
    print("Ceil of %s is" % x, ceil_of_x(arr, x))
    print("Floor of %s is" % x, floor_of_x(arr, x))
    arr = [1, 3, 3, 1, 2, 1, 1]
    print("Majority element is", majority_element(arr))
    arr = [1, 2, 3, 3, 3, 3, 10]
    x = 1
    print("%s Is Majority" % x, check_for_majority(arr, x))
    arr = [1, 3, 20, 4, 1, 0]
    print("Peak index is", find_peak(arr))
    arr = [-10, -5, 0, 3, 7]
    print("Fixed Point", find_fixed_point(arr))
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    subarray_sum_equal_to_x(arr, 12)
    print("Maximum triplet sum", max_triplet_sum(arr))
    print("smallest triple", smallest_diff_triplet([15, 12, 18, 9], [10, 17, 13, 8], [14, 16, 11, 5]))
    print("triplet sum to given value", triplet_sum(arr, 11))
