class Solution:
    def findDuplicate(self, nums) -> int:
        l, r = 1, len(nums) - 1
        while l+1 < r:
            count = 0
            mid = l + (r - l) // 2
            for i in nums:
                if i < mid:
                    count += 1
            if count < mid:
                l = mid
            else:
                r = mid - 1
        return l if nums.count(l)>1 else r