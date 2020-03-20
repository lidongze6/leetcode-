class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imin = nums[0]
        imax = nums[0]
        res = float("-inf")
        for i in range(1, len(nums)):
            cur_max = max(imax * nums[i], imin * nums[i], nums[i])
            cur_min = min(imax * nums[i], imin * nums[i], nums[i])
            res = max(res, cur_max)
            imax = cur_max
            imin = cur_min
        return res
