def expressionExpand(s):
    _, res = helper(s, 0)
    return res


def helper(s, p):
    res = ""
    multi = ""
    while p < len(s):
        if s[p].isalpha():
            res += s[p]
        elif s[p].isdigit():
            multi += s[p]
        elif s[p] == "[":
            p, tmp = helper(s, p + 1)
            res += tmp * int(multi)
            multi = ""
        elif s[p] == "]":
            return p, res
        p += 1
    return p, res


s = "3[a2[c]]"
print(expressionExpand(s))
