def searchRange(nums, target):
    if nums == []:
        return [-1, -1]
    res = [-1, -1]
    l1, r1 = 0, len(nums) - 1
    while l1 < r1:
        mid = l1 + (r1 - l1) // 2
        if nums[mid] >= target:
            r1 = mid
        else:
            l1 = mid + 1
    if l1 >= r1 and nums[l1] == target:
        res[0] = l1

    l2, r2 = 0, len(nums) - 1
    while l2 < r2:
        mid = l2 + (r2 - l2 + 1) // 2
        if nums[mid] <= target:
            l2 = mid
        else:
            r2 = mid - 1
    if l2 >= r2 and nums[l2] == target:
        res[1] = l2

    return res


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
