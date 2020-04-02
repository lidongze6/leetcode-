class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        # 前缀和
        l = len(nums)
        if l <= 1: return False
        pre_sum = [0] * (l + 1)
        for i in range(1, l + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        for i in range(l):
            for j in range(i + 2, l + 1):
                if k == 0:
                    if pre_sum[j] - pre_sum[i] == 0:
                        return True
                elif (pre_sum[j] - pre_sum[i]) % k == 0:
                    return True
        return False


nums = [5, 0, 0]
k = 0
print(Solution().checkSubarraySum(nums, k))
