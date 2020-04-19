class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        # 考虑使用dict,若前面存在出现的等差数列，则当前数字长度为其等差数字长度+1
        # 否则当前数字的长度为1
        l = len(arr)
        if l <= 1: return l
        f = dict()

        for i in range(l):
            if arr[i] - difference in f:
                f[arr[i]] = f[arr[i] - difference] + 1
            else:
                f[arr[i]] = 1

        return max(f.values())


arr=[4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
k=0
print(Solution().longestSubsequence(arr,k))