"""
Print all combinations of points that can compose a given number.
You can win three kinds of basketball points, 1 point, 2 points and 3 points. Given a total score n, print out all the
combination to compose n.
"""


def combination(n, s):
    if n < 0:
        return
    if n == 0:
        print(s)
        return
    for i in [1, 2, 3]:
        s.append(i)
        combination(n - i, s)
        s.pop()


n = 10
combination(n, [])
