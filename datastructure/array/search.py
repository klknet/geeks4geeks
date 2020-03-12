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


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8]
    x = 16
    print("have pair of sum equals to x", sum_pair_as_x(arr, x))
    print("have pair of sum equals to x", pair_sum_as_x_hash(arr, x))
    arr = [2, 4, 5, 7, 7, 6]
    print("element at index", search_in_step_arr(arr, 2, 7))
