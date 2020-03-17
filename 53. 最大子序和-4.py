class Solution:
    def maxSubArray(self, nums) -> int:
        # 前缀和
        pre_sum = [0] * (len(nums) + 1)
        res = float("-inf")
        min_sum = pre_sum[0]
        for i in range(1, len(nums) + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            res = max(res, pre_sum[i] - min_sum)
            min_sum = min(min_sum, pre_sum[i])
        return res


nums = [-1]
print(Solution().maxSubArray(nums))
