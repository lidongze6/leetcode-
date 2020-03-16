def leastBricks(wall):
    #前缀和，且统计前缀和出现的最大次数
    from collections import Counter
    c = Counter({0: 0})
    for col in wall:
        pre_sum = [0] * (len(col) - 1)
        for i in range(len(col) - 1):
            if i == 0:
                pre_sum[i] = col[i]
            else:
                pre_sum[i] = pre_sum[i - 1] + col[i]
        c.update(Counter(pre_sum))
    res = c.most_common(1).pop()[1]
    return len(wall) - res


wall = [[1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]]

print(leastBricks(wall))
