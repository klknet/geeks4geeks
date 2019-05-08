"""
Boyer Moore Algorithm - Bad Character Heuristic.
The idea of bad character heuristic is simple. The character of the text which doesn't match with the current character of
pattern is called the bad character. Upon mismatch, we shift the pattern until-
1)The mismatch become a match.
2)Pattern p move past the mismatch character.
"""

no_of_chars = 256


def bm_search(pat, txt):
    m, n = len(pat), len(txt)
    bad_char = [-1] * no_of_chars
    i = 0
    for k in range(m):
        bad_char[ord(pat[k])] = k
    while i <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[i + j]:
            j -= 1
        if j<0:
            print(i)
            i += (m-bad_char[ord(txt[i+m])] if i+m<n else 1)
        else:
            i += max(j-bad_char[ord(txt[i+j])], 1)


pat = 'ABCA'
txt = 'ABACAABCACD'
bm_search(pat, txt)
