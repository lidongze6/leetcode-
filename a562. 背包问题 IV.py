class Solution:
    """
    给出n个物品,以及一个数组,nums[i]代表第i个物品的大小,
    保证大小均为正数并且没有重复,正整数 target 表示背包的大小,
    找到能填满背包的方案数。每一个物品可以使用无数次
    """
    def backPackIV(self, nums, target):
        l = len(nums)
        if l == 0: return 0
        f = [[0] * (target + 1) for i in range(l + 1)]  # f[i][j] #前i个物品拼出j重量的方法数

        for i in range(l + 1):  # 前i个物品拼出0重量的方法均为1
            f[i][0] = 1

        for i in range(1, l + 1):
            for j in range(1, target + 1):
                f[i][j] += f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] += f[i][j - nums[i - 1]]

        return f[-1][-1]