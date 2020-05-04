class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数DP dp[i]=dp[j-1]*dp[i-j](j from 1..i)
        if n == 1: return 1
        dp = [0] * (n + 1)  # dp[i]表示1..i为节点组成的二叉树的个数
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
