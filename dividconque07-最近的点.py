def nearestpoint(nums):
    # 给一组点，找到最近的两个点

    nums.sort()
    l, r = 0, len(nums) - 1
    _, res = helper(nums, l, r)
    return res


def helper(nums, l, r):
    if l + 1 == r:
        return (nums[r] - nums[l]), [nums[l], nums[r]]
    elif l == r:
        return float("inf"), [nums[l], nums[r]]
    mid = l + (r - l) // 2
    left_min, left_res = helper(nums, l, mid)
    right_min, right_res = helper(nums, mid + 1, r)

    l = nums[mid + 1] - nums[mid]
    if l <= min(left_min, right_min):
        return l, [nums[mid], nums[mid] + 1]
    elif left_min < right_min:
        return left_min, left_res
    elif left_min >= right_min:
        return right_min, right_res


nums = [20, 7, 14, 5, 10, 33, 41, 29, 65, 49]
print(nearestpoint(nums))
