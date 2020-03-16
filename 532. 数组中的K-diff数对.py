class Solution:
    def findPairs(self, nums, k):
        if not nums or k<0: return 0
        nums = sorted(nums)
        l, r = 0, 1
        count = 0
        s = set()
        while l < len(nums) and r < len(nums):
            if r > l:
                if nums[r] - nums[l] == k and (nums[l], nums[r]) not in s:
                    count += 1
                    s.add((nums[l], nums[r]))
                    l += 1
                    r += 1
                elif nums[r] - nums[l] < k:
                    r += 1
                elif nums[r] - nums[l] > k:
                    l += 1
                else:
                    r+=1
            else:
                while r <= l:
                    r += 1
        return count


nums = [3, 1, 4, 1, 5]
k = 2
print(Solution().findPairs(nums, k))
