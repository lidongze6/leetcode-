def largestRectangleArea(heights):
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