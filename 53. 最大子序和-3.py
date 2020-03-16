def maxSubArray(nums):
    # 动态规划:O(n)
    cur_sum = 0
    res = nums[0]
    for i in range(len(nums)):
        if cur_sum > 0:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
        res = max(res, cur_sum)
    return res
