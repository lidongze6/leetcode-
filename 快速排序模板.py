def quicksort(nums, start, end):
    if start >= end: return

    l, r = start, end
    mid = nums[(l + r) // 2]
    while l <= r:  # 当交叉时才停止
        while l <= r and nums[l] < mid: l += 1
        while l <= r and nums[r] > mid: r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if nums[r] == mid:
        r -= 1
    elif nums[l] == mid:
        l += 1

    quicksort(nums, start, r)
    quicksort(nums, l, end)


nums = [21, 3, 45, 130, 77, 71, 25, 86, 60, 101, 103]
start, end = 0, len(nums) - 1
quicksort(nums, start, end)
print(nums)
