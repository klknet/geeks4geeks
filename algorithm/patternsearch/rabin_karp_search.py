"""
Rabin-Karp Algorithm for Pattern Searching.
Rabin-Karp algorithm matches the hash value of the pattern with the hash value of the current substring of text, and if
the hash values match then it only starts matching individual characters. So Rabin-Karp algorithm needs to calculate hash
values for following strings.
1)Pattern itself.
2)All the substrings of txt of length m.
Therefore, the numeric value is calculated using modular arithmetic to make sure that the hash values can be stored in an
integer variable. To do rehashing, we need to take off the most significant digit and add the new least significant digit
for in hash value. Rehashing is done using following formula.
hash(txt[s+1..s+m]) = (R*(hash(txt[s..s+m-1] - txt[s]*h) + txt[s+m]) mod q

hash(txt[s..s+m-1]): hash value at shift s.
hash(txt[s+1..s+m]): hash value at next shift.
R: the number of characters in the alphabet.
q: a prime number.
h: R^(m-1)
"""


def rk_search(txt, pat):
    n, m = len(txt), len(pat)
    t = 0
    p = 0
    h = 1
    q = 101 # quotient, A prime number
    R = 256 # carry
    # calculate pow(R, m-1) % q
    for i in range(m-1):
        h = (h*R)%q
    # calculate the hash value of m characters of txt and pat
    for i in range(m):
        t = (R * t + ord(txt[i])) % q
        p = (R * p + ord(pat[i])) % q
    for i in range(n-m):
        if t == p:
            for k in range(m):
                if txt[i+k] != pat[k]:
                    break
                k += 1
            if k == m:
                print('Pattern found at index', i)
        else:
            if i < n-m-1:
                t = (R * (t-ord(txt[i])*h) + ord(txt[i+m])) % q
                if t<0:
                    t = t+q


txt = 'GEEKS FOR GEEKS'
pat = 'GEEK'
rk_search(txt, pat)
