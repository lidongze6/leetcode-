def subset(nums):
    lst = []
    res = []
    subset_helper(lst, nums, 0, res)
    return res


def subset_helper(lst, nums, startindex, res):
    res.append(lst[:])

    for i in range(startindex, len(nums)):
        lst.append(nums[i])
        subset_helper(lst, nums, i + 1, res)
        lst.pop()


print(subset([1, 2, 3]))
