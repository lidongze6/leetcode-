class Solution:
    def largestDivisibleSubset(self, nums):
        l = len(nums)
        if l <= 1: return nums
        nums.sort()
        f = [1] * l  # 第i个元素结尾能找到的最大子集

        res = [i for i in range(l)]

        for i in range(1, l):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)

                    if f[i] == f[j] + 1:
                        res[i] = j
        max_v = max(f)
        ans = []
        for i in range(l - 1, -1, -1):
            if f[i] == max_v:
                ans.append(nums[i])
                start = i
                break

        for i in range(max_v-1):
            ans.append(nums[res[start]])
            start = res[start]
        return ans[::-1]


nums = [1, 2, 4, 8]
print(Solution().largestDivisibleSubset(nums))
