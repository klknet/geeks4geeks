# Sort an array in wave form
def sort_in_wave(arr):
    n = len(arr)
    for i in range(0, n, 2):
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


def sort_in_wave1(arr):
    arr.sort()
    n = len(arr)
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]


if __name__ == '__main__':
    arr = [5, 8, 6, 7, 89, 74, 35, 14]
    print(arr)
    sort_in_wave1(arr)
    print(arr)
