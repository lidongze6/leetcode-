def longestWPI(hours):
    list = [1 if i > 8 else -1 for i in hours]
    presum = [0] * (len(list) + 1)
    for j in range(1, len(list) + 1):
        presum[j] = presum[j - 1] + list[j - 1]

    res = 0
    stack = []
    for i in range(len(presum)):
        if not stack or presum[stack[-1]] > presum[i]:
            stack.append(i)

    for j in range(len(presum))[::-1]:
        while stack and presum[stack[-1]] < presum[j]:
            res = max(res, j - stack.pop())
    return res