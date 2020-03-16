def isIsomorphic(s: str, t: str) -> bool:
    dict1 = {}
    dict2 = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in dict1 and t[i] not in dict2:
            dict1[s[i]] = t[i]
            dict2[t[i]] = s[i]
        elif s[i] in dict1 and t[i] in dict2:
            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]:
                return False
        else:
            return False
    return True


s = "paper"
t = "title"
print(isIsomorphic(s, t))
