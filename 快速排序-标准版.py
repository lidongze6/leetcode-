def quicksort(nums):
    start, end = 0, len(nums) - 1

    quicksort_helper(nums, start, end)


def quicksort_helper(nums, start, end):
    # base
    if start >= end:
        return
    l, r = start, end
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quicksort_helper(nums, start, l - 1)
    quicksort_helper(nums, r + 1, end)


nums = [3, 21, 3, 45, 130, 77, 71, 25, 3, 86, 60, 101, 21, 103]
print(quicksort(nums))
print(nums)
