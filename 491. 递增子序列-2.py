class Solution:
    def findSubsequences(self, nums):
        if len(nums) <= 1:
            return []
        res = []

        self.helper(nums, [], res, 0)
        return res

    def helper(self, nums, tmp, res, index):
        if len(tmp) >= 2:
            res.append(tmp[:])
        visited = set()
        for i in range(index, len(nums)):
            if (tmp and nums[i] < tmp[-1]) or nums[i] in visited:
                continue
            tmp.append(nums[i])
            visited.add(nums[i])
            self.helper(nums, tmp, res, i + 1)
            tmp.pop()
