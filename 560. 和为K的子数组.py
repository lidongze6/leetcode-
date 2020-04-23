class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # 初始化哈希表hash={0:1}，表示累加和为0，出现了1次。
        dict1 = {0:1}
        count = 0
        pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            count += dict1.get(pre_sum[i] - k, 0)
            dict1[pre_sum[i]] = dict1.get(pre_sum[i], 0) + 1
        return count


nums=[1,-1,1,1,1]
k=2
print(Solution().subarraySum(nums,k))