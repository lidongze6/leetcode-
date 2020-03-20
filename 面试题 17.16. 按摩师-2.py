class Solution:
    def massage(self, nums):
        # dfs+记忆化,超时
        def helper(cur):
            f = [-1] * len(nums)
            if cur == -1: return 0
            if cur == 0: return nums[0]
            if f[cur] != -1:
                return f[cur]
            else:
                f[cur] = max(helper(cur - 1), helper(cur - 2) + nums[cur])
                return f[cur]

        return helper(len(nums) - 1)


nums = [183, 219, 57, 193, 94, 233, 202, 7, 88, 80, 112, 78, 135, 62, 228, 247, 211]
print(Solution().massage(nums))
