"""
Search for all permutations.

1)Store counts of frequencies of pattern in first count array countP[]. Also store counts of frequencies of characters
in first window of text in array countTW[].
2)Now run a loop from i=M to N-1, do following in loop:
 a)If the two count arrays are identical, we found an occurrence.
 b)Increment count of current character of text in countTW[].
 c)Decrement count of first character of previous window in countTW[].
3)The last window is not checked by above loop. so explicitly check it.
"""

no_of_chars = 256


def anagram_search(pat, txt):
    m, n = len(pat), len(txt)
    pat_count = [0] * no_of_chars
    cur_count = [0] * no_of_chars
    for i in range(m):
        pat_count[ord(pat[i])] += 1
        cur_count[ord(txt[i])] += 1
    for i in range(m, n):
        if compare(pat_count, cur_count, pat):
            print(i - m)
        cur_count[ord(txt[i])] += 1
        cur_count[ord(txt[i - m])] -= 1
        if i == n - 1:
            if compare(pat_count, cur_count, pat):
                print(n - m)


def compare(patCount, curCount, pat):
    m = len(pat)
    for j in range(m):
        if patCount[ord(pat[j])] != curCount[ord(pat[j])]:
            return False
    return True


pat = "ABCD"
txt = "BACDGABCDA"
anagram_search(pat, txt)
