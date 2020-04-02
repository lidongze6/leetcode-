class Solution:
    def findTargetSumWays(self, nums, S: int):
        # 背包型DP，主要注意j的范围判定
        l = len(nums)
        s = sum(nums)
        if S > s or S < -s: return 0

        m = 2 * s + 1
        f = [[0] * m for i in range(l + 1)]  # f[i][j] 前i个数和为j的个数

        f[0][s] = 1

        # 前i个数和为i的个数为1,f[i][i]=1
        # 前0个数和为j的个数为0,f[0][j]=0
        for i in range(1, l + 1):
            for j in range(0, m):
                if j - nums[i - 1] >= 0:
                    f[i][j] += f[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] <= m - 1:
                    f[i][j] += f[i - 1][j + nums[i - 1]]
        return f[l][S + s]


nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))
