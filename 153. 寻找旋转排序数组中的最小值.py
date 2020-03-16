def findMin(nums) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= nums[r]:
            r = mid
        else:
            l = mid + 1
    if l>=r:
        return nums[l]

nums=[3,4,5,1,2]
print(findMin(nums))
