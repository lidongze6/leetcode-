def minAddToMakeValid(S):
    stack=[]
    for i in S:
        if stack and  i==")" and stack[-1]=="(":
            stack.pop()
        else:
            stack.append(i)
    return len(stack)



S="()))(("
print(minAddToMakeValid(S))