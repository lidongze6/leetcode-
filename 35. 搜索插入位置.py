def searchInsert(nums, target):
    l, r = 0, len(nums)-1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
    if nums[l] == target: return l
    if nums[r] == target: return r
    if nums[r] < target:
        return r + 1
    if nums[l] > target:
        return l
    if nums[l] < target < nums[r]:
        return r

print(searchInsert([1,3,5,6],7))




