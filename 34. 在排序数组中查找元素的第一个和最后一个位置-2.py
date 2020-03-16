def searchRange(nums, target):
    res = [-1, -1]

    def findFirst(nums, target):
        l, r = 0, len(nums) - 1
        if not nums:
            return -1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif target == nums[mid]:
                r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        else:return -1

    def findLast(nums, target):
        l, r = 0, len(nums) - 1
        if not nums:
            return -1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif target == nums[mid]:
                l = mid
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        else:return -1
    res[0] = findFirst(nums, target)
    res[1] = findLast(nums, target)
    return res

print(searchRange([5,6,7,8,8,10],8))