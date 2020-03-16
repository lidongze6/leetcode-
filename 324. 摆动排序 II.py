def wiggleSort(nums):
    start, end = 0, len(nums) - 1
    quicksort(nums, start, end)
    mid=(len(nums)+1)//2
    nums[0::2], nums[1::2] = reversed(nums[:mid]), reversed(nums[mid:])


def quicksort(nums, start, end):
    if start >= end:
        return
    l, r = start, end
    mid = nums[(l + r) // 2]
    while l <= r:
        while l <= r and nums[l] < mid:
            l += 1
        while l <= r and nums[r] > mid:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    quicksort(nums, start, r)
    quicksort(nums, l, end)


nums = [4,5,5,6]
wiggleSort(nums)
print(nums)
