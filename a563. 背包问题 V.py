class Solution:
    """
    给出n个物品, 以及一个数组, nums[i]代表第i个物品的大小,
    保证大小均为正数, 正整数target表示背包的大小, 找到能填满背包的方案数。
    每个物品可重复使用多次
    """

    def backPackV(self, nums, target):
        # 简化内存
        if not nums: return 0
        l = len(nums)
        f = [[0] * (target + 1) for i in range(l + 1)]  # f[i][j] 前i个物品装j重量的方法数
        f[0][0] = 1
        for i in range(l + 1):
            f[i][0] = 1

        for i in range(1, l + 1):
            for j in range(1, target + 1):
                f[i][j] += f[i - 1][j]
                if j - nums[i - 1] >= 0:
                    f[i][j] += f[i - 1][j - nums[i - 1]]

        return f[-1][-1]