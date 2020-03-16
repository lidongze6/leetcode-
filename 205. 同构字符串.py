def isIsomorphic(s, t):
    dict1 = dict()
    l1 = len(s)
    l2 = len(t)
    if l1 != l2:
        return False

    for i in range(l1):
        if s[i] not in dict1 or t[i] not in dict1:
            dict1[s[i]] = t[i]
            dict1[t[i]] = s[i]
        else:
            if dict1[s[i]] != t[i] or dict1[t[i]] !=s[i]:
                return False
    return True


if __name__ == "__main__":
    s = "ab"
    t = "aa"
    print(isIsomorphic(s, t))
