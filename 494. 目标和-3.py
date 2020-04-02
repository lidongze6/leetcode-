class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        # dfs+记忆化
        l = len(nums)
        dic = dict()

        def dfs(cur, target):
            if cur == l:
                if target == S:
                    return 1
                else:
                    return 0
            if (cur, target) in dic:
                return dic[(cur, target)]
            else:
                res = dfs(cur + 1, target + nums[cur - 1]) + dfs(cur + 1, target - nums[cur - 1])
                dic[(cur,target)]=res
                return res
        return dfs(0,0)

nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))
