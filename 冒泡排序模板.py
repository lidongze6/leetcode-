def bubble_sort(nums):
    if not nums or len(nums) == 1:
        return nums

    l = len(nums)
    while l > 1:
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        l -= 1


nums = [21, 3, 45, 130, 77, 60, 71, 25, 86, 60, 101, 103]
bubble_sort(nums)
print(nums)
