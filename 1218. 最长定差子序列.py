class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        # 正常DP，但超时了，故想到进行优化，见方法2
        l=len(arr)
        if l<=1:return l
        f=[1]*l

        for i in range(1,l):
            for j in range(i):
                if arr[i]-arr[j]==difference:
                    f[i]=max(f[i],f[j]+1)
        return max(f)