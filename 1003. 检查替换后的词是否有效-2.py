def isValid(S):
    stack=[]
    for c in S:
        if c=="b" and (not stack or (stack[-1] !="a")):
            return False
        elif c=="c" and (not stack or (stack[-1] !="b")):
            return False
        stack.append(c)
        if c == 'c':
            stack.pop()
            stack.pop()
            stack.pop()

    return len(stack)==0

S="abcabcababcc"
print(isValid(S))

