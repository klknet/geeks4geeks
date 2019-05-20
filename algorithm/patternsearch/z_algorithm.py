"""
Z algorithm (Linear time pattern searching Algorithm)
What is Z array?
For a string str[0..n-1], Z array is of same length as string. An element Z[i] of Z array stores length of the longest
substring starting from str[i] which is also a prefix of str[0..n-1]. The first entry of Z is meaningless as complete
string is always prefix of itself.
The idea is to concatenate pattern and text, and create a string P$T where P is pattern, $ is a special character should
not be present in pattern and text, and T is text. Build the Z array for concatenated string. In Z array, if Z value at
any point is equal to pattern length, then pattern is present at that point.

We can construct Z array in linear time.
The idea is to maintain an interval [L, R] which is the interval with max R such that [L, R] is prefix substring.
1)If i>R then there is no prefix substring that starts before i and ends after i, so we reset L and R and compute new
[L, R] by comparing str[0..] and str[i..] and get Z[i]=R-L+1
2)If i<=R then let k=i-L, now Z[i]>=min(Z[k], R-i+1) because str[i..] matches str[k..] for at least R-i+1 characters (they
are in [L,R] interval which we know is a prefix substring)
 Now two sub cases arise.
 a) If Z[k]<R-i+1 then there is no prefix substring starting at str[i] so Z[i] = Z[k] and interval remains same.
 b) If Z[k]>=R-i+1 then it is possible to extend the interval thus we will set L as i and start matching from str[R]
 onwards and get new R then we will update interval and calculate Z[i] = R-L+1.
"""


def search(pat, txt):
    concat = pat + '$' + txt
    m, n = len(pat), len(concat)
    Z = getZArr(concat, n)
    for i in range(m + 1, n):
        if Z[i] == m:
            print(i - m - 1)


def getZArr(txt, n):
    Z = [0] * n
    L = R = 0
    for i in range(1, n):
        if i > R:
            L = R = i
            while R < n and txt[R - L] == txt[R]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - L + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < n and txt[R - L] == txt[R]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z


txt = 'Geeks for Geeks'
pat = 'Geek2'
search(pat, txt)
