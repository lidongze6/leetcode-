def helper(S, p, res):
    while p < len(S):
        if S[p].isalpha():
            res += S[p]
        elif S[p].isdigit():
            if p + 1 < len(S) and S[p + 1].isdigit():
                tmp, p = helper(S, p + 1, res * int(S[p]))
                res = tmp
            else:
                res = res * int(S[p])
                tmp, p = helper(S, p + 1, "")
                res += tmp
                return res, p
        p += 1
    return res, p


S = "ha22w41da"
print(helper(S, 0, ""))
