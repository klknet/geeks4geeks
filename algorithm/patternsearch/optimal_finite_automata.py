"""
Efficient Construction of Finite Automata.
Algorithm
1)Fill the first row. All entries in first row are always 0 except the entry for pat[0] character. For pat[0] character
we always need to go to state 1.
2)Initialise the lps as 0. lps for the first index is always 0.
3)Do following for rows at index i=1 to M.(M is the length of the pattern).
  a)Copy the entries from the row at index equal to lps.
  b)Update the entry for pat[i] character to i+1
  c)Update lps=TF[lps][pat[i]]
"""

no_of_chars = 256


def search(pat, txt):
    n, m = len(txt), len(pat)
    TF = computeTF(pat, m)
    state = 0
    for i in range(n):
        state = TF[state][ord(txt[i])]
        if state == m:
            print(i - m + 1)


def computeTF(pat, m):
    TF = [[0 for col in range(no_of_chars)] for row in range(m + 1)]
    lps = 0
    TF[0][ord(pat[0])] = 1
    for state in range(1, m+1):
        for x in range(no_of_chars):
            TF[state][x] = TF[lps][x]
        if state<m:
            TF[state][ord(pat[state])] = state+1
            lps = TF[lps][ord(pat[state])]
    return TF


pat = 'AABA'
txt = 'AABAACAADAABAAABAA'
search(pat, txt)
