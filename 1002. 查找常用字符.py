def commonChars(A):
    s = set(A[0])
    for word in A:
        res = s & set(word)
        s = res
    ret = []
    for w in list(s):
        tmp = 100
        for c in A:
            tmp = min(c.count(w), tmp)
        ret += w * tmp
    return ret