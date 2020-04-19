class Solution:
    # 有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。
    # 每件物品只能用一次。体积是volums，重量是weight，价值是cost。
    # 输出最大价值
    def backPack(self, M: int, V: int, weight: list, volums: list, cost: list):
        l = len(weight)
        dp = [[0] * (V + 1) for i in range(M + 1)]

        for i in range(1, l + 1):
            for j in range(M, weight[i-1] - 1, -1):
                for k in range(V, volums[i-1] - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - weight[i-1]][k - volums[i - 1]] + cost[i - 1])
        print(dp[-1][-1])
