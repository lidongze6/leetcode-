class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP 维护一个最大数组，一个最小数组
        ma, mi = [0] * len(nums), [0] * len(nums)
        ma[0], mi[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            ma[i] = max(nums[i], max(ma[i - 1] * nums[i], mi[i - 1] * nums[i]))
            mi[i] = min(nums[i], min(ma[i - 1] * nums[i], mi[i - 1] * nums[i]))

        return max(ma)