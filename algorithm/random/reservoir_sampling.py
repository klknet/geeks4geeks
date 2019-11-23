"""
Reservoir sampling.
"""
import random


def sampling(stream, k):
    reservoir = stream[:k]
    for i in range(k, len(stream)):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir


def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        if j < i:
            arr[i], arr[j] = arr[j], arr[i]
    return arr



stream = [1, 2, 3, 4, 5, 6,
          7, 8, 9, 10, 11, 12]
print(sampling(stream, 5))
print(shuffle([1, 2, 3, 4, 5, 6, 7, 8]))
