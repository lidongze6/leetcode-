class Solution:
    # 求最大价值的总方案数，以01背包为例
    def backPack(self, m: int, weight: list, value: list):
        l = len(weight)
        dp = [float("-inf")] * (m + 1)
        dp[0] = 0
        # dp[i]表示恰好装下重量j时的背包的最大价值是多少
        g = [0] * (l + 1)
        g[0] = 1
        # g[i]表示恰好装下重量j时的背包的最大价值的方案数
        MOD = 10 ** 9 + 7  # 防止方案数量太大

        for i in range(1, l + 1):
            for j in range(m + 1, weight[i - 1] - 1, -1):  # 注意这里是逆序遍历
                tmp = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
                s = 0
                if tmp == dp[j]:
                    s += g[j]
                if tmp == dp[j - weight[i - 1]] + value[i - 1]:
                    s += g[j - weight[i - 1]]
                s = s % MOD
                dp[j] = tmp
                g[j] = s
        # 计算取得最大价值时的总方案数
        max_v = 0
        for i in range(1, m + 1):
            max_v = max(max_v, dp[i])
        res = 0
        for i in range(1, m + 1):
            if dp[i] == max_v:
                res += g[i]
            res = res % MOD if res >= MOD else res
        return res



weight = [2, 3, 5, 7]
value = [1, 5, 2, 4]
m = 10
print(Solution().backPack(m,weight,value))

