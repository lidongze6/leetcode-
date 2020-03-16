def findTheDifference(s: str, t: str) -> str:
    set1 = set(s)
    set2 = set(t)
    if set1 != set2:
        res = set2 - set1
    else:
        res = [l for l in s if s.count(l) != t.count(l)]
    return res.pop()