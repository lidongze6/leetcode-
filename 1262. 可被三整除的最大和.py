class Solution:
    def maxSumDivThree(self, nums) -> int:
        l = len(nums)
        dp = [[float("-inf")] * 3 for i in range(l)]

        dp[0][nums[0] % 3] = nums[0]

        for i in range(1, l):
            tmp = nums[i] % 3
            dp[i][(0 + tmp) % 3] = max(dp[i - 1][(0 + tmp) % 3], dp[i - 1][0] + nums[i], nums[i])
            dp[i][(1 + tmp) % 3] = max(dp[i - 1][(1 + tmp) % 3], dp[i - 1][1] + nums[i])
            dp[i][(2 + tmp) % 3] = max(dp[i - 1][(2 + tmp) % 3], dp[i - 1][2] + nums[i])

        return dp[-1][0] if dp[-1][0] != float("-inf") else 0


nums = [2,19,6,16,5,10,7,4,11,6]
print(Solution().maxSumDivThree(nums))
