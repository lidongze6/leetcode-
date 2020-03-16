def findWords(words):
    line1, line2, line3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    res = []
    for w in words:
        s = set(w.lower())
        if s.issubset(line1) or s.issubset(line2) or s.issubset(line3):
            res.append(w)
    return res
