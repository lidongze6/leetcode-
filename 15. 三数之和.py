class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                elif nums[l] + nums[r] == -num:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
