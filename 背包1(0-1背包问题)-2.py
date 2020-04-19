class Solution:
    # 空间优化，二维DP---》一维DP
    def backPack(self, m: int, weight: list, value: list):
        l = len(weight)
        dp = [0] * (m + 1)
        # dp[i]表示装重量j的背包的最大价值是多少

        for i in range(1, l + 1):
            for j in range(m + 1, -1, -1):  # 注意这里是逆序遍历
                if j - weight[i - 1] >= 0:
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])

        return dp[-1]
