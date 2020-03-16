def topKFrequent(words, k):
    s = list(set(words))
    s.sort(key=lambda x: (-words.count(x), x))
    return s[:k]


def topKFrequent_2(words, k):
    from collections import Counter
    c = Counter(words)
    res = list(c.keys())
    res.sort(key=lambda x:(-c[x],x))
    return res


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "is", "day"]
k = 4
print(topKFrequent_2(words, k))
