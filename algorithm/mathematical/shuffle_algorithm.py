"""
Shuffle a given array using Fisher-Yates shuffle algorithm.
The idea is to start with the last element, swap it with a randomly selected element from the whole array(including last).
"""
import random


def shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        idx = random.randint(0, i)
        arr[idx], arr[i] = arr[i], arr[idx]


arr = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(arr)
print(arr)
