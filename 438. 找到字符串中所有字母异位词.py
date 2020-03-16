def findAnagrams(s, p):
    dict1 = {}
    for c in p: dict1[c] = dict1.get(c, 0) + 1
    res = []
    ret = dict()
    l, r = 0, 0
    while l <= len(s) - len(p):
        if s[r] not in dict1:
            r += 1
            l = r
            ret.clear()
        else:
            ret[s[r]] = ret.get(s[r], 0) + 1
            if r - l + 1 == len(p):
                if ret==dict1:
                    res.append(l)
                ret[s[l]] -= 1
                l += 1
            r += 1
    return res


s = "cbaebabacd"

p = "abc"
print(findAnagrams(s, p))
