def countCharacters(words, chars):
    from collections import Counter
    c = Counter(chars)
    res = 0
    for w in words:
        if len(Counter(w) - c) == 0:
            res += len(w)
    return res