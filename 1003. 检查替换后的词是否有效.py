def isValid(S):
    stack=[]
    for i in S:
        if not stack:
            if i=="a": stack.append(i)
            else: return False
        elif stack and stack[-1]=="b":
            if i=="b":return False
            elif i=="c" and stack[-2]=="a":
                stack.pop()
                stack.pop()
            else:stack.append(i)
        elif stack and stack[-1]=="a":
            if i=="c":return False
            else:stack.append(i)
    if len(stack)==0:
        return True

S="cababc"
print(isValid(S))


