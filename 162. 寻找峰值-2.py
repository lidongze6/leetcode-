class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        if l == r: return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid
        if l == 0 or nums[l - 1] < nums[l] and nums[l + 1] < nums[l]:
            return l
        if r == len(nums) - 1 or nums[r - 1] < nums[r] and nums[r + 1] < nums[r]:
            return r


nums = [1, 2]
print(Solution().findPeakElement(nums))
