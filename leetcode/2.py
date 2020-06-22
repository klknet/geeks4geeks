def lengthOfLongestSubstring(s):
    res = -1
    for i in range(len(s)):
        c = 1
        h = set(s[i])
        for j in range(i+1, len(s)):
            if s[j] in h:
                break
            c += 1
            h.add(s[j])
        res = max(res, c)
    return res


def lengthOfSubstring(s):
    res = 0
    h = set()
    i = j = 0
    while i < len(s):
        while j<len(s) and s[j] not in h:
            h.add(s[j])
            j+=1
        res=max(res,j-i)
        if j==len(s):
            break
        h.remove(s[i])
        i+=1
    return res


print(lengthOfLongestSubstring("dvdf"))
print(lengthOfSubstring("pwwkew"))
print(lengthOfSubstring("dvdf"))
