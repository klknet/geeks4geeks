# Sort n numbers in range from 0 to n^2-1 in linear time
def sort1ton2(arr, n):
    # Do counting sort for first digit in base n, Note that instead of passing digit number, exp(n^0=1) is passed.
    count_sort(arr, n, 1)
    count_sort(arr, n, n)


def count_sort(arr, n, exp):
    count = [0] * n
    output = [0] * n
    for i in range(n):
        count[arr[i] // exp % n] += 1
    for i in range(n - 1):
        count[i + 1] += count[i]
    for i in range(n - 1, -1, -1):
        pos = arr[i] // exp % n
        output[count[pos] - 1] = arr[i]
        count[pos] -= 1
    for i in range(n):
        arr[i] = output[i]


if __name__ == '__main__':
    arr = [40, 12, 45, 32, 33, 1, 22]
    print(arr)
    sort1ton2(arr, len(arr))
    print(arr)
