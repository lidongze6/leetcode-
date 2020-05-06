class Solution:
    def numberOfSteps(self, num: int) -> int:
        # DP O(n) 超时
        if num == 0: return 0
        if num == 1: return 1
        dp = [0] * (num + 1)
        dp[1] = 1
        for i in range(2, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2] + 1
            else:
                dp[i] = dp[i - 1] + 1

        return dp[-1]
