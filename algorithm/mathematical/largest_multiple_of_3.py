"""
Find the largest multiple of 3.
1.Sort the array in non-decreasing order.
2.Take three queues. One for storing elements which on dividing by 3 gives reminder as 0. The second queue stores digits
which on dividing by 3 gives reminder as 1. The third queue stores digits which on dividing by 3 gives reminder as 2.
Call them as queue0, queue1, queue2.
3.Find the sum of all the digits.
4.Three cases arise:
.....4.1.The sum of digits is divisible by 3. Dequeue all the digits from the three queues. Sort them in non-increasing
order, output the array.
.....4.2.The sum of digits produces reminder 1 when divide by 3.
Remove one item from queue1. If queue1 is empty, remove two items from queue2, if queue2 contains less than 2 items, the
number is not possible.
.....4.3.The sum of digits produces reminder 2 when divide by 3.
Remove one item from queue2. If queue2 is empty, remove two items from queue1, if queue1 contains less than 2 items, the
number is not possible.
5.Finally empty all the queues into an auxiliary array. Sort the auxiliary array in non-increasing order, output the array.
"""


def largest_multiple(arr):
    arr = sorted(arr, key=lambda k: k)
    q_0 = []
    q_1 = []
    q_2 = []
    for i in arr:
        r = i % 3
        if r == 0:
            q_0.append(i)
        elif r == 1:
            q_1.append(i)
        elif r == 2:
            q_2.append(i)
    s = sum(arr)
    r = s % 3
    res = []
    if r == 0:
        return arr.reverse()
    elif r == 1:
        if len(q_1) > 0:
            q_1.pop(0)
        elif len(q_2) > 1:
            q_2.pop(0)
            q_2.pop(1)
    else:
        if len(q_2) > 0:
            q_2.pop(0)
        elif len(q_1) > 1:
            q_1.pop(0)
            q_1.pop(1)
    sorted(q_0 + q_1 + q_2, key=lambda x: x, reverse=True)
    return res


print(largest_multiple([8, 1, 7, 6, 0]))
