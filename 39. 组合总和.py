def combinationSum(nums, target):
    if not nums:
        return []
    n = len(nums)
    res = []
    nums.sort()

    def combinationSum_helper(i, tmp, target):
        if target == 0:
            res.append(tmp)
            return
        if i == n or target < nums[i]:
            return
        combinationSum_helper(i, tmp + [nums[i]], target - nums[i])
        combinationSum_helper(i + 1, tmp, target)

    combinationSum_helper(0, [], target)
    return res
