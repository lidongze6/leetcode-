class Solution:
    def moveZeroes(self, nums):
        p, z = 1, 0
        while z < len(nums) and p < len(nums):
            while z < len(nums) and nums[z] != 0:
                z += 1
            while p < len(nums) and nums[p] == 0 or p < z:
                p += 1
            if z < len(nums) and p < len(nums):
                nums[z], nums[p] = nums[p], nums[z]
                z += 1
                p += 1
        return nums


nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(Solution().moveZeroes(nums))
