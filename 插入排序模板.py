def insert_sort(nums):
    if not nums or len(nums) == 1:
        return nums

    l = len(nums)
    for i in range(1, l):
        j = i - 1
        tmp = i
        while j >= 0:
            if nums[tmp] < nums[j]:
                nums[tmp], nums[j] = nums[j], nums[tmp]
                tmp -= 1
                j -= 1
            else:
                break


nums = [21, 3, 45, 130, 77, 71, 25, 86, 60, 101, 103]
insert_sort(nums)
print(nums)
