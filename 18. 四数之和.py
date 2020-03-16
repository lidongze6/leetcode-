def fourSum(nums, target):
    # 回溯法--超时
    res = []
    tmp = []
    helper(nums, target, res, tmp, 0)
    return res


def helper(nums, target, res, tmp, startindex):
    if target == 0 and len(tmp) == 4:
        res.append(tmp[:])
        return res
    for i in range(startindex, len(nums)):
        if i != startindex and nums[i] == nums[i - 1]:
            continue
        tmp.append(nums[i])
        helper(nums, target - nums[i], res, tmp, i + 1)
        tmp.pop()

    return res


nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
print(fourSum(nums, target))
