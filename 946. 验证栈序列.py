def validateStackSequences(pushed,popped):
    """
    模拟栈的操作
    当push一个数入stack时，这个数正好对应popped栈底的数，则将stack和popped同时pop掉
    注：stack pop栈顶，popped pop栈底（因为栈底对应的永远都是第一个弹出栈的元素）
    :param pushed:
    :param popped:
    :return:
    """
    stack=[]
    for i in pushed:
        stack.append(i)
        while stack and stack[-1]==popped[0]:
            stack.pop()
            popped.pop(0)

    return len(stack)==0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed,popped))
