class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d > target: return 0
        if d == target: return 1
        dp = [[0] * (target + 1) for i in range(d + 1)]
        # dp[i][j] 表示前i个骰子掷出j的方法
        dp[0][0] = 1
        MOD = 10**9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                dp[i][j] = 0
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= MOD
        return dp[-1][-1]


d, f, target = 30, 30, 500
print(Solution().numRollsToTarget(d, f, target))
