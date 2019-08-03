"""
Print all combinations of r elements in a given array of size n.
Method 1.
Start from first index and one by one fix elements at this index and recur for remaining indexes.
Method 2.
Include and exclude every element.
"""


def combination(arr, cur, idx, temp, r):
    if cur == r:
        print(temp)
        return
    while idx < len(arr) and len(arr)-idx >= r-cur:
        temp[cur] = arr[idx]
        combination(arr, cur + 1, idx + 1, temp, r)
        idx += 1


def comb(arr, cur, r, idx, temp):
    if cur == r:
        print(temp)
        return
    if idx < len(arr):
        # include current
        temp[cur] = arr[idx]
        comb(arr, cur+1, r, idx + 1, temp)
        # exclude current
        comb(arr, cur, r, idx + 1, temp)


arr = list(set([1, 2, 3, 4, 5]))
r = 3
data = [0] * r
combination(arr, 0, 0, data, r)
print()
comb(arr, 0, r, 0, data)
