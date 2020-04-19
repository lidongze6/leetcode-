class Solution:
    # 空间优化
    def backPack(self, m: int, weight: list, value: list):
        """:param m: 最大载重量
        :param weight: 每个物品的重量
        :param value: 每个物品的价值
        :return: 能装下的最大价值
        """
        l=len(weight)
        dp = [0] * (m + 1)

        for i in range(1, l + 1):
            for j in range(weight[i-1],m + 1): # 正向遍历，且j-weight[i-1]>=0，故j直接从weight[i-1]遍历
                dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])

        print(dp[-1])