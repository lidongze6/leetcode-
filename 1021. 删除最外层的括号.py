def removeOuterParentheses(S):
    # 递归
    l = len(S)
    count = 0
    for i in range(l - 1):
        if S[i] == "(":
            count += 1
        else:
            count -= 1
            if count == 0:
                return removeOuterParentheses(S[:i + 1]) + removeOuterParentheses(S[i + 1:])

    return S[1:l - 1]


S="(()())(())(()(()))"
print(removeOuterParentheses(S))