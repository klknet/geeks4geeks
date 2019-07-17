"""
DFA based division.

"""


def DFA_division(n, k):
    FA = build_DFA(k)
    return division_util(FA, n)


def build_DFA(k):
    FA = []
    for state in range(k):
        item = [0]*2
        trans0 = state * 2
        item[0] = trans0 if trans0 < k else trans0 - k

        trans1 = state * 2 + 1
        item[1] = trans1 if trans1 < k else trans1 - k
        FA.append(item)
    return FA


def division_util(FA, n):
    b = bin(n)[2:]
    state = 0
    for c in b:
        state = FA[state][c == '1']
    return state


n, k = 21, 7
print(DFA_division(n, k))
