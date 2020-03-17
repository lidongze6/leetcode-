class Solution:
    # DP 自下而上
    # time:O(n),space:O(n)
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs_2(self, n):
        first, second = 1, 1
        res = 1  # 当n为1的时候，不执行for循环，直接返回res
        for i in range(2, n + 1):
            res = first + second
            first, second = second, res
        return res
