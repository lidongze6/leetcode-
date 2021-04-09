class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

nums = [1,3,5,6]
print(Solution().binary_search(nums,7))
