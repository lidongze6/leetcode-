def sortColors(nums):
    """
    双指针：类似于荷兰国旗问题，等于1的在左边，等于2的在中间，等于3的在右边
    """
    l, r = -1, len(nums)
    i = 0
    while i < r:
        if nums[i] == 0:
            l += 1
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
        elif nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            r -= 1
            nums[i], nums[r] = nums[r], nums[i]
    return nums


nums=[2,0,2,1,1,0]
print(sortColors(nums))
