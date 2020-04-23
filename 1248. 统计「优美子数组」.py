class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        # 前缀和，统计出现奇数的次数
        # 问题简化成求presum[j]-presum[i]=k的个数
        # 简化为求子数组和为k的个数的问题
        # 同leetcode 560
        dic = {0: 1}
        pre_sum = [0] * (len(nums) + 1)
        res = 0
        for i in range(1, len(nums) + 1):
            if nums[i - 1] % 2 == 1:
                pre_sum[i] = pre_sum[i - 1] + 1
            else:
                pre_sum[i] = pre_sum[i - 1]
            res += dic.get(pre_sum[i] - k, 0)
            dic[pre_sum[i]] = dic.get(pre_sum[i], 0) + 1

        return res

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(Solution().numberOfSubarrays(nums,k))