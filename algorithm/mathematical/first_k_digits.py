"""
Print first k digits of 1/n where n is a positive integer.
"""


def first_k_digit(n, k):
    res = []
    rem = 1
    for i in range(k):
        res.append(int(rem * 10 / n))
        rem = (rem * 10) % n
    return res


"""
Given a number as string, find the number of contiguous subsequences which recursively add up to 9.
"""


def num_of_contiguous(s):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '9':
            print(s[i], end=" ")
            count += 1
        c = int(s[i])
        for j in range(i + 1, n):
            c = (c + int(s[j])) % 9
            if c == 0:
                print(s[i:j + 1], end=' ')
                count += 1
    return count


print(first_k_digit(21, 4))
print(num_of_contiguous('4189'))
