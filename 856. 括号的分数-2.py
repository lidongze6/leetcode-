def scoreOfParentheses(S):
    l, r = 0, len(S) - 1
    return helper(S, l, r)


def helper(S, l, r):
    if S[l:r + 1] == "()":
        return 1
    stack = []
    count = 0
    for i in range(l, r):  # 遍历到len(S)-1
        if S[i] == "(":
            stack.append(S[i])
            count += 1
        elif S[i] == ")":
            stack.pop()
            count -= 1
            if not stack:
                # len(S)步之前达到平衡，是(A)((B))的类型
                return helper(S, l, i) + helper(S, i + 1, r)
    # len(S)-1步还没有达到平衡，说明是((A))的类型
    return 2 * helper(S, l + 1, r - 1)


S = "(()(()))"
print(scoreOfParentheses(S))
