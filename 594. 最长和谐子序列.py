def findLHS(nums):
    from collections import Counter
    c = Counter(nums)
    s = c.keys()
    res = 0
    for nu in s:
        if nu + 1 in c:
            res = max(res, (c[nu] + c[nu + 1]))
    return res


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))
