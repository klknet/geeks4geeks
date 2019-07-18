"""
Given a number, find the next smallest palindrome.
We will start with two indices i and j. i pointing to the two middle elements. We one by one move i and j away from
each other.
Step1. Ignore the part of left side which is same as the corresponding part of right side. For example, if the number
is 8 3 4 2 2 4 6 9, we ignore the four middle elements, i now points to elements 3 and j points to elements 6.
Step2. After step 1, following two cases arise.
Case1: i and j cross the boundary.
This case occurs when the input number is palindrome. In this case, we only add 1 to the middle digit. propagate the carry
towards MSB digit of left side and simultaneously copy mirror of the left side to the right side.
Case2: there are digits left between left side and right side are not same. So we just mirror the left side to the right
side & try to minimise the number formed to guarantee the next smallest palindrome.
2.1)All we need to check is the digit just after ignored part in step 1. If this digit is greater than the corresponding
digit in right side digit, then copy left side to the right side is sufficient and we don't need to do anything else.
2.2)This happens when above defined digit of left side is smaller. We handle this subcase like case 1. We just add 1 to
the middle digit, propagate the carry towards to the MSB digit of left side and simultaneously copy mirror of left side
to the right side.
"""


def next_palindrome(serial):
    n = len(serial)
    if n == 0:
        return
    i = j = 0
    if n & 1 == 0:
        i = int(n / 2) - 1
        j = int(n / 2)
    else:
        i = j = int(n / 2)
    m = i
    while i >= 0 and j < n and serial[i] == serial[j]:
        i -= 1
        j += 1
    if i < 0:
        add_one(serial, m)
    elif serial[i] >= serial[j]:
        copy_left_2_right(serial, i, j)
    elif serial[i] < serial[j]:
        add_one(serial, i)


def add_one(serial, k):
    while True:
        m_val = serial[k] + 1
        if m_val > 9:
            serial[k] = m_val - 10
            k -= 1
        else:
            serial[k] = m_val
            break
        if k < 0:
            serial.insert(0, 1)
            break
    n = len(serial)
    if n & 1 == 0:
        i = int(n / 2) - 1
        j = int(n / 2)
    else:
        i = j = int(n / 2)
    copy_left_2_right(serial, i, j)


def copy_left_2_right(serial, i, j):
    while i >= 0:
        serial[j] = serial[i]
        i -= 1
        j += 1


serial = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
serial = [9, 9, 9, 9]
serial = [7, 8, 3, 3, 2, 2]
serial = [7, 1, 3, 3, 2, 2]
next_palindrome(serial)
print(serial)
