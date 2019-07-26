"""
Reservoir Sampling.
"""
import random


def reservoir_sampling(stream, n, k):
    reservoir = stream[:k]
    for i in range(k, n):
        r = random.randint(0, i)
        if r < k:
            reservoir[r], stream[i] = stream[i], reservoir[r]
    return reservoir


stream = list(range(100))
print(reservoir_sampling(stream, len(stream), 10))
