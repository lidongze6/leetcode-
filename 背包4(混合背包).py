class Solution:
    # 物品一共有三类：
    # 第一类物品只能用1次（01背包）；
    # 第二类物品可以用无限次（完全背包）；
    # 第三类物品最多只能用 si 次（多重背包）；
    def backPack(self, m: int, weight: list, value: list, nums: list):
        l=len(weight)
        dp = [0] * (m + 1)

        for i in range(1, l + 1):
            if nums[i - 1] == -1:
                for j in range(m, weight[i - 1] - 1, -1):   # 注意遍历顺序
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
            elif nums[i - 1] == 0:
                for j in range(weight[i - 1], m + 1):   # 注意遍历顺序
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
            else:
                for j in range(m, -1, -1):   # 注意遍历顺序
                    k = 0
                    while k <= nums[i - 1] and j - k * weight[i - 1] >= 0:
                        dp[j] = max(dp[j], dp[j - k * weight[i - 1]] + k * value[i - 1])
                        k += 1
        print(dp[-1])