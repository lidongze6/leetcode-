def removeKdigits(num: str, k: int) -> str:
    stack = []  # 记录最小值
    for i in num:
        if stack==[] or int(stack[-1])<=int(i):
            stack.append(i)
        else:
            while stack and int(stack[-1]) > int(i) and k:
                stack.pop()
                k -= 1
            stack.append(i)
    if k:
        stack[-k:]=[]
    str1="".join(stack) if stack else 0
    return int(str1)





num="5337"
k=2
print(removeKdigits(num,k))