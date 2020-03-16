class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        l, r = 0, 0
        tmp = 1
        res = 0
        while r < len(nums):
            tmp *= nums[r]
            while l <= r and tmp >= k:
                tmp //= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res


nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))
