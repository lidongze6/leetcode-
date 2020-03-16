def quicksort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums if i < pivot]
        equal = [j for j in nums if j == pivot]
        large = [x for x in nums if x > pivot]
    return quicksort(less) + equal + quicksort(large)


nums = [3, 21, 3, 45, 130, 77, 71, 25, 3, 86, 60, 101, 21, 103]
print(quicksort(nums))
