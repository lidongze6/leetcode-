class Solution:
    def makesquare(self, nums):
        # DFS+记忆化
        l = len(nums)
        nums.sort()
        if l < 4 or sum(nums) % 4 != 0:
            return False
        target = sum(nums) // 4
        dic = dict()

        def dfs(nums, count, remain):
            if count == 3 and remain == 0:
                return True
            if (tuple(nums), count, remain) in dic:
                return dic[(tuple(nums), count, remain)]
            else:
                for i in range(len(nums)):
                    if remain + nums[i] < target:
                        res = dfs(nums[:i] + nums[i + 1:], count, remain + nums[i])
                        dic[(tuple(nums[:i] + nums[i + 1:]), count, remain+nums[i])] = res
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
        return dfs(nums,0,0)


nums=[1,1,2,2,2]
print(Solution().makesquare(nums))