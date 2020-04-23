class Solution:
    # 求最大价值具体方案，以01背包为例
    def backPack(self, m: int, weight: list, value: list):
        l = len(weight)
        f = [[0] * (m + 1) for i in range(1 + l)]
        pi = []
        for i in range(1, l + 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j]
                if j - weight[i - 1] >= 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - weight[i - 1]] + value[i - 1])

        j = m
        for i in range(l, 0, -1):  # 从后往前遍历，因为最终res为f[l][m]，也即倒着搜寻f[l][m]是从哪来的
            if j >= weight[i - 1] and f[i][j] == f[i - 1][j - weight[i - 1]] + value[i - 1]:
                pi.append(i - 1)  # 第i个物品，也即index为i-1
                j -= weight[i - 1]
        return pi[::-1]


weight = [2, 3, 5, 7]
value = [1, 5, 2, 4]
m = 10
print(Solution().backPack(m, weight, value))
