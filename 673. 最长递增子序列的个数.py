class Solution:
    def findNumberOfLIS(self, nums) -> int:
        l = len(nums)
        if l <= 1: return l
        f = [1] * l
        c = [1] * l
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    if f[j] + 1 > f[i]:  # 代表第一次遇到最长子序列
                        f[i] = max(f[j] + 1, f[i])
                        c[i] = c[j]
                    elif f[j] + 1 == f[i]:  # 代表之前已经遇到过最长子序列
                        c[i] += c[j]
        res, tmp = 0, max(f)
        for i in range(l):
            if f[i] == tmp:
                res += c[i]
        return res


nums=[1,3,5,4,7]
print(Solution().findNumberOfLIS(nums))