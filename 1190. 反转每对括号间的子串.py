def reverseParentheses(s):
    from collections import deque
    stack=[]
    deqe=deque()

    for char in s:
        if char==")":
            while stack[-1] !="(":
                deqe.append(stack.pop())
            stack.pop() # 把"(" 弹出
            while deqe:
                stack.append(deqe.popleft())
        else:
            stack.append(char)

    return "".join(stack)


s="(abcd)"
print(reverseParentheses(s))