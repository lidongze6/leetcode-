class Solution:
    def canPartition(self, nums) -> bool:
        # 背包型DP
        l = len(nums)
        if l < 2: return False
        div, mod = divmod(sum(nums), 2)
        if mod != 0: return False

        f = [[False] * (div + 1) for i in range(l+1)] # f[i][j] #前i个物品装重量j能否装下
        # 求f[l][div]
        for i in range(l+1):
            f[i][0]=True

        for i in range(1,l+1):
            for j in range(1, div + 1):
                f[i][j]=f[i-1][j]
                if j>=nums[i-1]:
                    f[i][j] |=f[i-1][j-nums[i-1]]

        return f[l][div]

nums=[1,2,5]
print(Solution().canPartition(nums))