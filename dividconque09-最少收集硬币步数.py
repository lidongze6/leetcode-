def minstep(nums):
    l, r = 0, len(nums) - 1
    if l >= r:
        return 1

    high = min(nums)
    mid = nums.index(high)
    nums=[i-high for i in nums]

    return min(r - l, minstep(nums[l:mid]) + minstep(nums[mid:r]) + high)


nums = [3, 1, 2, 5, 1]
print(minstep(nums))
