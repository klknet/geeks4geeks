"""
Select a random number from stream with O(1) space.
1)Initialize 'count' as 0, count is used to store count of numbers seen so far in stream.
2)For each number X from stream, do following.
.....a)Increment count by 1.
.....b)If count is 1, set result as x, and return result.
.....c)Generate a random number from 0 to count-1. Let the generated random number be i.
.....d)If i is equal to count-1, update result as x.
"""
import random


def random_pick(stream, stop):
    count = 0
    X = None
    print(stop, end=' ')
    for line in stream.readlines():
        count += 1
        if count == 1:
            X = line
        if count == stop:
            break
        idx = random.randint(0, count)
        if idx == count - 1:
            X = line
    return int(X)


stream = open("../other/number.txt", "r")
for i in range(64):
    stream.seek(0, 0)
    print(random_pick(stream, random.randint(1, 1 << 15)))
stream.close()
