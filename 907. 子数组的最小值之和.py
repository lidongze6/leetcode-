def sumSubarrayMins(A):
    """
    解题思路：
    （1）：找寻以当前元素为左边界和右边界时，可以分别向右和向左延伸几个元素
            所构成的子序列的最小还是该元素，例如[3,1,2,4]以2位左边界则[2,4]是最长的元素
            以2位右边界，则只有[2]时是最长的
            又或者以1位左边界则[1,2,4]是最长的，右边界[3,1]是最长的
    （2）：记录该元素i最小的子序列个数为公式：left*right 其中left为左边的最长长度，right为右边的最长长度
    （3）：要注意序列中出现相同数字的情况，故求左和求右只能一边有“=”号，防止重复计算
    :param A:
    :return:
    """
    l = len(A)
    left_stack = [[0, -1]]  # [当前的值,自己的位置]
    left = [0] * l # 记录索引
    right_stack = [[0, l]]
    right = [0] * l #记录索引
    res = 0

    for n, i in enumerate(A):
        while left_stack and i < left_stack[-1][0]:
            left_stack.pop()

        left[n] = left_stack[-1][1]
        left_stack.append([i, n])

    for j in range(l - 1, -1, -1):
        while right_stack and A[j] <= right_stack[-1][0]:
            right_stack.pop()

        right[j] = right_stack[-1][1]
        right_stack.append([A[j], j])

    for i in range(l):
        res = res + (i - left[i]) * (right[i] - i) * A[i]

    return res


A = [71, 55, 82, 55]
print(sumSubarrayMins(A))
