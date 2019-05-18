"""
Aho-Corasick Algorithm for pattern search.
1.Preprocessing: Build an automation of all words in arr[] the automation has mainly three functions
  Go to: This function simply follows edges of trie of all words in arr[]. It is represented as a 2D array go[][] where
        we stored next state for current state and character.
  Failure: This function stores all edges that are followed when current character doesn't have edge in trie. It is
        represented as 1D arr f[] where we store next state for current state.
  Output: Store indexes of all words that end at current state. It is represented as 1D array o[] where we store indexes
        of all matching words as a bitmap for current state.
2. Traverse the given txt over built automation to find all matching words.
"""

maxc = 256
maxs = 12
g = [[-1 for ch in range(maxc)] for state in range(maxs)]
f = [-1] * maxs
o = [0] * maxs


def search(txt, arr):
    k = len(arr)
    n = len(txt)
    buildAutoMachine(arr, k)
    currentState = 0
    for i in range(n):
        currentState = findNextState(ord(txt[i]), currentState)
        if currentState == 0:
            continue
        for j in range(k):
            if o[currentState] & (1 << j):
                print('Words', arr[j], 'appears from', i - len(arr[j]) + 1, i)


def findNextState(ch, state):
    # while next state not defined, find the failure funciton
    while g[state][ch] == -1:
        state = f[state]
    return g[state][ch]


def buildAutoMachine(arr, k):
    state = 0
    # build goto function
    for i in range(k):
        currentState = 0
        s = arr[i]
        for j in range(len(s)):
            if g[currentState][ord(s[j])] == -1:
                state += 1
                g[currentState][ord(s[j])] = state
            currentState = g[currentState][ord(s[j])]
        o[state] |= (1 << i)
    # build failure function
    queue = []
    f[0] = 0
    for i in range(maxc):
        if g[0][i] != -1:
            queue.append(g[0][i])
            # depth 1 failed to root
            f[g[0][i]] = 0
        else:
            g[0][i] = 0
    # using bfs build failure function
    while len(queue) > 0:
        state = queue.pop()
        for i in range(maxc):
            # find the deepest proper prefix
            if g[state][i] != -1:
                failureState = f[state]
                while g[failureState][i] == -1:
                    failureState = f[failureState]
                failureState = g[failureState][i]
                f[g[state][i]] = failureState
                o[g[state][i]] |= o[failureState]
                queue.insert(0, g[state][i])


arrs = ['he', 'she', 'hers', 'his']
txt = 'ahishers'
search(txt, arrs)
