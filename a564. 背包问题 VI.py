class Solution:
    """
    给出n个物品, 以及一个数组, nums[i]代表第i个物品的大小,
    保证大小均为正数, 正整数target表示背包的大小, 找到能填满背包的方案数。
    每个物品可重复使用多次，且装物品的顺序不同算不同的方法
    """
    def backPackIV(self, nums, target):
        if not nums: return 0
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    f[i] += f[i - num]

        return f[-1]


nums = [2,3,6,7]
target = 7
print(Solution().backPackIV(nums,target))