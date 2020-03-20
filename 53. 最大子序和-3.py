def maxSubArray(nums):
    # 动态规划:O(n)
    # if max_sum[i-1]>0: max_sum[i]=max_sum[i-1]+nums[i]
    # elif max_sum[i-1]<0: max_sum[i]=nums[i]
    # res=max(res,max_sum)
    cur_sum = nums[0]
    res = nums[0]
    for i in range(1,len(nums)):
        if cur_sum >= 0:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
        res = max(res, cur_sum)
    return res
