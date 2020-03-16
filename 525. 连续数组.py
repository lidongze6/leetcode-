def findMaxLength(nums):
    # 两个单调栈,夹中间的值,仿照1124题
    list1 = [-1 if i == 0 else 1 for i in nums]
    pre_sum = [0] * (len(list1) + 1)
    for i in range(1, len(pre_sum)):
        pre_sum[i] = pre_sum[i - 1] + list1[i - 1]

    stack1 = []
    for i in range(len(pre_sum)):
        if not stack1 or stack1[-1][1] > pre_sum[i]:
            stack1.append([i, pre_sum[i]])

    stack2=[]
    for i in range(len(pre_sum)):
        if not stack2 or stack2[-1][1] < pre_sum[i]:
            stack2.append([i, pre_sum[i]])

    res=0
    for j in range(len(pre_sum))[::-1]:
        while stack1 and  pre_sum[j] > stack1[-1][1]:
            stack1.pop()
        while stack1 and pre_sum[j] == stack1[-1][1]:
            index, value = stack1.pop()
            res = max(res, j - index)

    for j in range(len(pre_sum))[::-1]:
        while stack2 and  pre_sum[j] < stack2[-1][1]:
            stack2.pop()
        while stack2 and pre_sum[j] == stack2[-1][1]:
            index, value = stack2.pop()
            res = max(res, j - index)
    return res


nums = [0,1,1]
print(findMaxLength(nums))
