def isAnagram(s, t):
    from collections import Counter
    c1 = Counter(s)
    c2 = Counter(t)
    return c1 == c2


def isAnagram_1(s, t):
    dict1 = {}
    if len(s) != len(t): return False
    for i in range(len(s)):
        dict1[s[i]] = dict1[s[i]] + 1 if s[i] in dict1 else 1

    for j in range(len(t)):
        if t[j] not in dict1:
            return False
        else:
            dict1[t[j]] -= 1
            if dict1[t[j]] == 0:
                dict1.pop(t[j])

    return True if not dict1 else False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
