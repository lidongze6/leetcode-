class Solution:
    def findSubsequences(self, nums):
        if len(nums) < 2:
            return []
        self.res = []
        tmp = []
        self.visit = set()
        self.dfs(tmp, 0, nums)
        return self.res

    def dfs(self, tmp, index, nums):
        if len(tmp) >= 2:
            self.res.append(tmp[:])
        for i in range(index, len(nums)):
            if i > index and nums[i - 1] == nums[i]:
                continue
            if tmp and nums[i] < tmp[-1]:
                continue
            if tuple(tmp+[nums[i]]) not in self.visit:
                tmp.append(nums[i])
                self.visit.add(tuple(tmp[:]))
                self.dfs(tmp, i + 1, nums)
                tmp.pop()
        return


nums = [1, 6, 7, 7, 1, 1, 1]
s = Solution()
print(s.findSubsequences(nums))
