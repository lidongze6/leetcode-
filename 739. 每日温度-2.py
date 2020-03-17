def dailyTemperatures(T):
    """
    逆序遍历
    ！！！求这个数后面的最大值基本上都是逆序遍历！！！
    :param T:
    :return:
    """
    stack=[]
    l=len(T)
    day=[0]*l
    for n,i in enumerate(range(l-1,-1,-1)):
        while stack and stack[-1][0]<=T[i]:
            stack.pop()
        if stack and stack[-1][0]>T[i]:
            day[l-n-1]=stack[-1][1]+n-l
        stack.append([T[i],l-n])

    return day


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))