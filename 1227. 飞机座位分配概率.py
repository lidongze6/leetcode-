class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1: return 1
        dp = [0] * (1 + n)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = float(1 / i) + (i - 2) / i * dp[i - 1]
        return dp[-1]


n = 3
print(Solution().nthPersonGetsNthSeat(n))
