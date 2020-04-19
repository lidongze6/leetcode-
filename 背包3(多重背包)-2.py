class Solution:
    # 空间优化成1维
    def backPack(self, m: int, weight: list, value: list, nums: list):
        """:param m: 最大载重量
        :param weight: 每个物品的重量
        :param value: 每个物品的价值
        :param nums: 每个物品的数量
        :return: 能装下的最大价值
        """
        l = len(weight)
        dp = [0] * (m + 1)

        for i in range(1, l + 1):
            for j in range(m, -1, -1):  # 逆序遍历，因为要用到前面的数
                k = 0
                while k <= nums[i - 1] and j - k * weight[i - 1] >= 0:
                    dp[j] = max(dp[j], dp[j - k * weight[i - 1]] + k * value[i - 1])
                    k += 1

        print(dp[-1])
