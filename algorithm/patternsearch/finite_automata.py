"""
Finite Automata algorithm for Pattern Searching.
In FA based algorithm, we preprocess the pattern and build a 2D array that represents a Finite Automata. Construction of
the FA is the main tricky part of this algorithm. Once the FA is build, the searching is simple. In search, we simply start
from the first state of the finite automata and the first character of the text. At every step, we consider next character
of the text, look for the next state in the build FA and move to a new state. If we reach the final state, then the pattern
is found in the text.
Number of states in FA will be M+1 where M is the length of the pattern. The main thing to construct FA is to get the next
state from the current state for every possible characters. Given a state k and a character x, we can get the next state
by considering the string 'pat[0..k-1]x' which is basically concatenation of pattern characters pat[0]...pat[k-1] and the
character x. The idea is to get length of the longest prefix of the given pattern such that the prefix is also suffix of
'pat[0..k-1]x'. The value of length gives us the next state.
"""

no_of_chars = 256


def search(pat, txt):
    m, n = len(pat), len(txt)
    TF = computTF(pat, m)
    state = 0
    for i in range(n):
        state = TF[state][ord(txt[i])]
        if state == m:
            print(i - m + 1)


def computTF(pat, m):
    TF = [[0 for col in range(no_of_chars)] for row in range(m + 1)]
    for state in range(m + 1):
        for x in range(no_of_chars):
            next_state = get_next_state(state, x, pat, m)
            TF[state][x] = next_state
    return TF


def get_next_state(state, x, pat, m):
    if state < m and x == ord(pat[state]):
        return state + 1
    for ns in range(state, 0, -1):
        if ord(pat[ns - 1]) == x:
            i = 0
            while i < ns - 1:
                if pat[i] != pat[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0


pat = 'AABA'
txt = 'AABAACAADAABAAABAA'
search(pat, txt)
