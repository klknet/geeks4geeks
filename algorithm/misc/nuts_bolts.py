"""
Nuts and Bolts Problem.
"""


def nuts_bolts(nuts, bolts):
    n = len(nuts)
    match_pair(nuts, bolts, 0, n-1)


def match_pair(nuts, bolts, low, high):
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])
        match_pair(nuts, bolts, low, pivot-1)
        match_pair(nuts, bolts, pivot+1, high)


def partition(arr, low, high, p):
    i = j = low
    while j < high:
        if ord(arr[j]) < ord(p):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif ord(arr[j]) == ord(p):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[high], arr[i] = arr[i], arr[high]
    return i


nuts = ['@', '#', '$', '%', '^', '&']
# nuts = ['5', '2', '8', '9', '1']
bolts = ['$', '%', '&', '^', '@', '#']
# bolts = ['9', '1', '8', '5', '2']
nuts_bolts(nuts, bolts)
print(nuts, bolts)