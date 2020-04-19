class Solution:
    # 时间优化，转化为O(mlogn)
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
            k = 1
            while k <= nums[i]:
                new_weight.append(weight[i] * k)
                new_value.append(value[i] * k)
                nums[i] -= k
                k *= 2
            if nums[i]:
                new_weight.append(weight[i] * nums[i])
                new_value.append(value[i] * nums[i])

        return max_value(new_weight, new_value)
