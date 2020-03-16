def helper(S, l, r, res):
    # 递归版本
    if S.isalpha():
        return S
    tmp = res
    for i in range(l, r):
        if S[i].isalpha():
            tmp += S[i]
        if S[i].isdigit():
            return helper(S, i + 1, r, tmp * int(S[i]))
    return tmp


S = "ha22w4"
K = 10
print(helper(S, 0, len(S), ""))
