def searchRange(nums, target):
    # 获取左边界
    l1, r1 = 0, len(nums) - 1
    while l1 + 1 < r1:
        mid = l1 + (r1 - l1) // 2
        if nums[mid] > target:
            r1 = mid
        elif nums[mid] < target:
            l1 = mid
        elif nums[mid] == target:
            r1 = mid

    if nums[l1] == target:
        return l1
    elif nums[r1] == target:
        return r1
    return -1


def searchRange_2(nums, target):
    # 获取右边界
    l1, r1 = 0, len(nums) - 1
    while l1 + 1 < r1:
        mid = l1 + (r1 - l1) // 2
        if nums[mid] > target:
            r1 = mid
        elif nums[mid] < target:
            l1 = mid
        elif nums[mid] == target:
            l1 = mid

    if nums[r1] == target:
        return r1
    elif nums[l1] == target:
        return l1
    return -1


nums = [1, 2, 2, 2, 2, 2, 3]
print(searchRange(nums, 2))
print(searchRange_2(nums, 2))
