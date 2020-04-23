def subsequence(arr):
    """
    Find all subsequences of a string.
    :param arr:
    :return:
    """
    res = []
    subsequence_util(arr, len(arr) - 1, res)
    return res


def subsequence_util(arr, n, res):
    if n == 0:
        res.append(arr[n])
        return
    subsequence_util(arr, n - 1, res)
    tmp = len(res)
    for i in range(tmp):
        res.append(res[i] + arr[n])
    res.append(arr[n])


def subsequence_bit(arr):
    n = len(arr)
    total = 2 ** n - 1
    res = []
    for counter in range(1, total + 1):
        r = ''
        for i in range(n):
            if counter & (1 << i):
                r += arr[i]
        res.append(r)
    return res


if __name__ == '__main__':
    arr = ['1', '2', '3', '4']
    print("subsequence", subsequence(arr))
    print("subsequence", subsequence_bit(arr))
