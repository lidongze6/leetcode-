def search(nums, target):
    if not nums:
        return False
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] == nums[l] and nums[mid] == nums[r]:
            r -= 1
            l += 1
        elif nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] <= nums[r]:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    if nums[l] == target or nums[r] == target:
        return True
    else:
        return False


nums = [3, 1, 1]
target = 3
print(search(nums, target))
