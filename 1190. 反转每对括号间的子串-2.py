def reverseParentheses(s):
    if not s or ")" not in s:
        return s
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            left = stack.pop()
            right = i
            return reverseParentheses(s[:left] + s[left + 1:right][::-1] + s[right + 1:])


s = "(u(love)i)"
print(reverseParentheses(s))
