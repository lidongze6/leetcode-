class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s = set()
            j = i + 1
            while j < len(nums):
                if -nums[i] - nums[j] in s:
                    res.append([nums[i], nums[j], -nums[i] - nums[j]])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                else:
                    s.add(nums[j])
                j += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
