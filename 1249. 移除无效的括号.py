def minRemoveToMakeValid(s):
    count = 0
    res = ""
    for char in s:
        if char.isalpha():
            res += char
        elif char == "(":
            count += 1
            res += char
        elif char == ")":
            if count > 0:
                res += char
                count -= 1
            else:
                continue

    res2 = ""
    if count > 0:
        for char1 in res[::-1]:
            if char1 == "(":
                if count > 0:
                    count -= 1
                else:
                    res2 += char1
            else:
                res2 += char1
        return res2[::-1]
    else:
        return res



s = "())()((("
print(minRemoveToMakeValid(s))
