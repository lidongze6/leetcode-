class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums or sum(nums) < S:
            return 0
        self.res = 0
        ret = []
        self.dfs(0, 0, nums, S, ret, [])
        return self.res, ret

    def dfs(self, tmpsum, index, nums, target,ret,tmp):
        if index == len(nums) and tmpsum == target:
            ret.append(tmp[:])
            self.res += 1
        if index < len(nums):
            for op in [1, -1]:
                tmp.append(nums[index]*op)
                tmpsum += nums[index] * op
                self.dfs(tmpsum, index + 1, nums, target,ret,tmp)
                tmpsum -= nums[index] * op
                tmp.pop()


nums = [1, 2, 3]
S = 2
s = Solution()
print(s.findTargetSumWays(nums, S))
