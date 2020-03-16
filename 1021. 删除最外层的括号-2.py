def removeOuterParentheses(S):
    stack = []
    count = 0
    for i, char in enumerate(S):
        if char == "(":
            if count != 0:
                stack.append(char)
            count += 1
        else:
            count -= 1
            if count != 0:
                stack.append(char)
    return "".join(stack)


S="(()())(())(()(()))"
print(removeOuterParentheses(S))