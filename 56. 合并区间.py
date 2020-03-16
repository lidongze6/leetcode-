def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    mid = len(intervals) // 2
    left = merge(intervals[:mid])
    right = merge(intervals[mid:])
    return judge(left, right)


def judge(left, right):
    res = []
    while left and right:
        if right[0][0] > left[-1][-1] or right[0][-1] < left[-1][0]:
            break
        else:
            le = left.pop()
            ri = right.pop(0)
            mi = min(le[0], ri[0])
            ma = max(le[1], ri[1])
            right.append([mi, ma])
    res = res + left + right

    return res


interval = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(merge(interval))

##TODO 有问题，在right.append还是left.append上有问题
