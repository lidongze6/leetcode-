def maxWidthRamp(A):
    # 单调栈的第二种用法，可以查找自己左边比自己小或大的数字的最远距离的最大值。
    stack = []
    res = 0
    for i, a in enumerate(A):  # 产生单调递减栈
        if not stack or A[stack[-1]] > a:
            stack.append(i)

    for j in range(len(A))[::-1]:  # 从后向前找，找到比自己小的，弹出并计算索引之差，直到遇到大的值，这里注意不入栈
        while stack and A[stack[-1]] <= A[j]:
            res = max(res, j - stack.pop())  # 若不弹出而是遍历，则还可以找出每个数字左边的比自己小活大的最远距离
            # 为什么要pop，因为是从后向前遍历，若后面的值使得单调递减栈里的值发生减少，则若前一个值比他大，减少的值
            # 一定能够满足比前面的值还小，则最远距离进行max比较即可
            # 若前一个比他小，则碰到此时栈顶的数一定也得停下来，而他的索引又比后一个小，故距离肯定比他小

    return res


A = [6, 2, 3, 4]
print(maxWidthRamp(A))
