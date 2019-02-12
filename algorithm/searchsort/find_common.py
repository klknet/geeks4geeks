# Find common elements in three sorted arrays


def find_common(a1, a2, a3):
    k, m, n = len(a1), len(a2), len(a3)
    i1 = i2 = i3 = 0
    common = []
    while i1 < k and i2 < m and i3 < n:
        if a1[i1] == a2[i2] == a3[i3]:
            i1 += 1
            i2 += 1
            i3 += 1
            common.append(i1)
        elif a1[i1] < a2[i2]:
            i1 += 1
        elif a1[i2] < a3[i3]:
            i2 += 1
        else:
            i3 += 1
    return common


if __name__ == '__main__':
    a1 = [1, 3, 5, 6, 7, 9]
    a2 = [2, 3, 5, 8, 10, 11]
    a3 = [-3, 4, 5, 8, 12]
    print(find_common(a1, a2, a3))
