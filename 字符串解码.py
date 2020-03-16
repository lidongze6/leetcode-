def helper(S):
    tmp = res = ""
    for i in range(len(S)):
        if S[i].isalpha():
            if i > 0 and S[i - 1].isdigit():
                tmp = ""
                tmp += S[i]
            else:
                tmp += S[i]
        if S[i].isdigit():
            tmp = tmp * int(S[i])
            res += tmp
    return res


S = "ha22w4"
print(helper(S))
