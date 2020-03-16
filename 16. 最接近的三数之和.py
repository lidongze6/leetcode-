class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        tmp = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r] + nums[i]
                if cur == target:
                    return target
                elif cur < target:
                    if abs(cur - target) < abs(tmp - target):
                        tmp = cur
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    if abs(cur - target) < abs(tmp - target):
                        tmp = cur
                    while l < r and nums[r] == nums[r - 1]:
                        r-=1
                    r -= 1
        return tmp


nums = [1, 1, -1]
target = 0
print(Solution().threeSumClosest(nums, target))
