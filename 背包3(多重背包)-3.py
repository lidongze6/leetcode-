class Solution:
    # 转化为0-1背包问题，比如物品1有3件，每件价值为2，我们不妨创建3个物品1，存在数组weight和数组value中
    def backPack(self, m: int, weight: list, value: list, nums: list):
        """:param m: 最大载重量
        :param weight: 每个物品的重量
        :param value: 每个物品的价值
        :param nums: 每个物品的数量
        :return: 能装下的最大价值
        """

        def max_value(weight: list, value: list):
            l = len(weight)
            dp = [0] * (m + 1)

            for i in range(1, l + 1):
                for j in range(m, weight[i - 1] - 1, -1):  # 免去了j-weight[i-1]>=0的判断
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])

        new_weight = []
        new_value = []
        for i in range(len(weight)):
            new_weight.extend([weight[i]] * nums[i])
            new_value.extend([value[i]] * nums[i])

        return max_value(new_weight, new_value)
