def findOcurrences(text, first, second):
    l, s = 0, 1
    text = text.split(" ")
    res = []
    while s < (len(text) - 1):
        if text[l] == first and text[s] == second:
            res.append(text[s + 1])
        l += 1
        s += 1
    return res