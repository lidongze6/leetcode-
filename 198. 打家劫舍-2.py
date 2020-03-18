class Solution:
    def rob(self, nums) -> int:
        # dfs 超时
        ans = float("-inf")

        def helper(cur, tmp):
            nonlocal ans
            if cur >= len(nums):
                if tmp > ans:
                    ans = tmp
                return
            helper(cur + 2, tmp + nums[cur])
            helper(cur + 1, tmp)

        helper(0, 0)
        return ans


nums = [1,2,3,1]
print(Solution().rob(nums))
