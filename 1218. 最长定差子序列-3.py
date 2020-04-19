class Solution:
    def longestSubsequence(self, arr, difference: int):
        # 用dp记录每个位置结尾的最长等差序列长度
        # 用indices记录最近一次出现的数字的位置
        dp = [1] * len(arr)
        indices = {}
        for i, num in enumerate(arr):
            if num - difference in indices:
                dp[i] = 1 + dp[indices[num - difference]]
            indices[num] = i
        return max(dp)


arr=[1,5,7,8,5,3,5,3,1]
k=-2
print(Solution().longestSubsequence(arr,k))
