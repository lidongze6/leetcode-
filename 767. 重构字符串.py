def reorganizeString(S):
    dict_c = {}
    res = ""
    for i in S:
        if i in dict_c:
            dict_c[i] += 1
        else:
            dict_c[i] = 1

    c = [[o, dict_c[o]] for o in dict_c]
    c.sort(key=lambda x: -x[1])
    if c[0][1] > len(S)//2+1:
        return "0"

    while len(c) >= 2:
        s1 = c.pop(0)
        s2 = c.pop(0)
        while s1[1] > 0 and s2[1] > 0:
            res = res + s1[0]
            res = res + s2[0]
            s1[1] -= 1
            s2[1] -= 1
        if s1[1] > 0:
            c.append(s1)
            c.sort(key=lambda x: -x[1])
        if s2[1] > 0:
            c.append(s2)
            c.sort(key=lambda x: -x[1])

    if len(c) == 1:
        s3 = c.pop()
        if s3[1] >= 2 or s3[0] == res[-1]:
            return "0"
        else:
            return res + s3[0]


S = "abbabbaaab"
print(reorganizeString(S))
