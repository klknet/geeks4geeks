"""
Lexicographic rank of string.
Let the given string be 'STRING'. In the input string, 'S' is the first character. There are total 6 characters and 4 of
them are smaller than 'S'. So there can be 4*5! smaller strings where first character smaller than 'S'.
Now let us Fix 'S' and find the smaller strings starting with 'S'.
Repeat the same process for T, rank is 4*5! + 4*4! + ...
Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! + ...
Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! + ...
Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + ...
Now fix N and repeat the same process for G, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0!
Rank is 597.
Note that the above computations find count of smaller strings. Therefore rank of given string is count of smaller strings
plus 1. The final rank is 598.
"""
import math


def find_rank(s):
    n = len(s)
    rank = 1
    mul = math.factorial(n)
    for i in range(n):
        less_count = 0
        for j in range(i + 1, n):
            if s[j] < s[i]:
                less_count += 1
        mul //= (n-i)
        rank += less_count * mul
    return rank


def find_rank_1(s):
    MAX_CHAR = 256
    count = [0]*MAX_CHAR
    for i in s:
        count[ord(i)] += 1
    for i in range(1, MAX_CHAR):
        count[i] += count[i-1]
    n = len(s)
    mul = math.factorial(n)
    rank = 1
    for i in range(n):
        mul = mul // (n-i)
        # remove a character ch from count[] array
        for j in range(ord(s[i]), MAX_CHAR):
            count[j] -= 1
        rank += mul*(count[ord(s[i])])
    return rank


print(find_rank('string'))
print(find_rank_1('string'))