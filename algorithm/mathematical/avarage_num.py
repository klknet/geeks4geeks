"""
Average of a stream of numbers.
"""


def average(numbers):
    s = 0
    n = len(numbers)
    for i in range(n):
        s += numbers[i]
        print(s / (i + 1))


average([10, 20, 30, 40, 50, 60])
