class Solution:
    # 每个物品有无限个
    def backPack(self, m: int, weight: list, value: list):
        """:param m: 最大载重量
        :param weight: 每个物品的重量
        :param value: 每个物品的价值
        :return: 能装下的最大价值
        """
        l=len(weight)
        dp = [[0] * (m + 1) for i in range(l + 1)]

        for i in range(1, l + 1):
            for j in range(m + 1):
                dp[i][j] = dp[i - 1][j]
                if j - weight[i - 1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - weight[i - 1]] + value[i - 1])

        print(dp[-1][-1])