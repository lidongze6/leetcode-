def maximalRectangle(matrix):
    res = 0
    list = [0] * len(matrix[0])
    for i in range(len(matrix)):
        list = [list[j] + 1 if matrix[i][j]=="1" else 0 for j in range(len(matrix[i]))]
        res = max(helper(list), res)
    return res


def helper(heights):
    stack = [[-1, 0]]
    res = 0
    l = len(heights)
    for n, h in enumerate(heights):
        if stack[-1][1] < h:
            stack.append([n, h])
        else:
            while stack[-1][1] > h:
                n1, h1 = stack.pop()
                tmp = n - stack[-1][0] - 1
                res = max(res, tmp * h1)
            stack.append([n, h])

    while len(stack) > 1:
        n1, h1 = stack.pop()
        tmp = l - stack[-1][0] - 1
        res = max(res, tmp * h1)

    return res


matrix = [["0", "1"], ["1", "0"]]

print(maximalRectangle(matrix))
