def quicksort(nums):
    if len(nums) <= 1:
        return nums
    start, end = 0, len(nums) - 1
    quick_helper(nums, start, end)
    return nums


def quick_helper(nums, start, end):
    if start >= end:  # Base
        return
    l, r = start, end
    mid = nums[(l + r) // 2]
    while l <= r:
        while l <= r and mid < nums[r]:
            r -= 1
        while l <= r and mid > nums[l]:
            l += 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if nums[r] == mid:
        r -= 1
    elif nums[l] == mid:
        l += 1
    # 最后...r,mid,l,... 即mid落在r与l之间，
    # 则下次排序在start--r 和 l---end排序即可
    quick_helper(nums, start, r)
    quick_helper(nums, l, end)


nums = [21, 3, 45, 130, 3, 77, 3, 30, 25, 86, 3, 60, 101]
print(quicksort(nums))
