"""
Find the largest multiple of 2，3，5.
Since the number must divisible by 2 and 5, it has to have last digit as 0. So if the given array doesn't contain any zero,
then no solution exists.
Once a zero is available, exact 0 from the given array. Only thing left is, the number should be is divisible by 3 and
the largest of all.
"""


def largest_multiple(arr):
    arr.sort(key=lambda k: k)
    exist = False
    for i in arr:
        if i == 0:
            exist = True
            break
    if not exist:
        return "no number can be formed"
    c = sum(arr)
    remainder = c % 3
    if remainder == 0:
        arr.reverse()
        return arr
    q_0, q_1, q_2 = [], [], []
    for i in arr:
        r = i % 3
        if r == 0:
            q_0.append(i)
        elif r == 1:
            q_1.append(i)
        elif r == 2:
            q_2.append(i)
    if remainder == 1:
        if len(q_1) > 0:
            q_1.pop(0)
        elif len(q_2) > 1:
            q_1.pop(0)
            q_1.pop(0)
        else:
            return "no number can be formed"
    elif remainder == 2:
        if len(q_2) > 0:
            q_2.pop(0)
        elif len(q_1) > 1:
            q_1.pop(0)
            q_1.pop(0)
        else:
            return "no number can be formed"
    return sorted(q_2 + q_1 + q_0, key=lambda k: k, reverse=True)


print(largest_multiple([1, 8, 7, 6, 0]))
print(largest_multiple([7, 7, 7, 6]))
