"""
given a value V, find the minimum change for V
1)Initialize result as empty.
2)find the largest denomination that is smaller than V.
3)Add found denomination to result, Subtract value of found denomination for V
4)If V becomes 0, then print the result,
Else repeat steps 2 and 3 for new value of V
"""

denomination = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def minimum_coin(v):
    result = []
    idx = len(denomination) - 1
    while v != 0:
        idx = find_largest(v, idx)
        result.insert(0, denomination[idx])
        v = v - denomination[idx]
    print(result)


def find_largest(v, idx):
    for i in range(idx, -1, -1):
        if denomination[i] <= v:
            return i


minimum_coin(25)