class Solution:
    def minSteps(self, n: int) -> int:
        # 判断n是否为素数
        if n <= 3: return n
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            j = 1
            while j <= i:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j - 1) + 1)
                j += 1

        return dp[n]


print(Solution().minSteps(9))
