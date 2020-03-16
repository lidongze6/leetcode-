def minSubArrayLen(s, nums) -> int:
    """
    时间复杂度o(n)的解法：双指针,遍历一趟
    """
    l, r = 0, 1
    res = len(nums)
    if sum(nums) < s: return 0
    sums = nums[0]

    while r < len(nums):
        while sums < s and r<len(nums):
            sums += nums[r]
            r+=1
        while sums >= s and l<r:
            res = min(res, r - l)
            sums-=nums[l]
            l+=1
    return res


s = 7
nums = [2, 3, 1, 2, 4, 3,7]
print(minSubArrayLen(s, nums))
