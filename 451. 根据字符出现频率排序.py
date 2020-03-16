def frequencySort(s):
    from collections import Counter
    c = Counter(s)
    r=list(s)
    r.sort(key=lambda x: -c[x])
    return "".join(r)


s = "tree"
print(frequencySort(s))
