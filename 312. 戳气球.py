class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        l = len(nums)
        f = [[0] * l for i in range(l)]  # f[i][j]: 从i到j位置的最大值

        for le in range(2, l):  # 步长，从2开始
            for i in range(l):  # 横坐标i，从1开始
                j = i + le
                if j > l - 1:  # 纵坐标小于l-1
                    break
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + nums[k] * nums[i] * nums[j])
        return f[0][l - 1]


nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))
