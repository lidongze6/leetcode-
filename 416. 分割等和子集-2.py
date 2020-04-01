class Solution:
    def canPartition(self, nums) -> bool:
        # dfs+记忆化 leetcode473
        l = len(nums)
        nums.sort()
        if l < 2 or sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dic = dict()

        def dfs(nums, count, remain):
            if count == 1 and remain == 0:
                return True
            if (tuple(nums), count, remain) in dic:
                return dic[(tuple(nums), count, remain)]
            else:
                for i in range(len(nums)):
                    if remain + nums[i] < target:
                        res = dfs(nums[:i] + nums[i + 1:], count, remain + nums[i])
                        dic[(tuple(nums[:i] + nums[i + 1:]), count, remain + nums[i])] = res
                        if res:
                            return True
                    elif remain + nums[i] == target:
                        res = dfs(nums[:i] + nums[i + 1:], count + 1, 0)
                        dic[(tuple(nums[:i] + nums[i + 1:]), count + 1, 0)] = res
                        if res:
                            return True
                    else:
                        break
            return False

        return dfs(nums, 0, 0)

nums=[1, 2, 3, 5]
print(Solution().canPartition(nums))