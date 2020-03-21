class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP time:O(n2) space:O(n)
        if not nums: return 0
        f = [1] * len(nums)  # f[i]表示前i个数所能构成的最大上升子序列，且nums[i]必须被选取
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
