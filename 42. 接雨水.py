def trap(height):
    stack = []
    res = 0
    for n, h in enumerate(height):
        if not stack or stack[-1][1] >= h:
            stack.append([n, h])
        else:
            while stack and stack[-1][1] < h:
                n1, h1 = stack.pop()
                if stack:
                    dis = n - stack[-1][0] - 1
                    hei = min(stack[-1][1], h) - h1
                    res += dis * hei
            stack.append([n, h])
    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
