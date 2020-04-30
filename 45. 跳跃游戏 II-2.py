class Solution:
    def jump(self, nums) -> int:
        # DP 超时
        l = len(nums)
        if l <= 1: return 0
        dp = [float("inf")] * l
        dp[0] = 0
        for i in range(1, l):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
