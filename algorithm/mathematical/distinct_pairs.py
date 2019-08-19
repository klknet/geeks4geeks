"""
Count distinct non-negative integer pairs( x,y) that satisfy the inequality x*x + y*y < n.
"""
import math


def count_pairs(n):
    upper = int(math.sqrt(n)) + 1
    res = []
    for x in range(upper):
        for y in range(n):
            if x * x + y * y < n:
                res.append((x, y))
            else:
                break
    return res


def count_climb_ways(n):
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


print(count_pairs(8))
print(count_climb_ways(4))
