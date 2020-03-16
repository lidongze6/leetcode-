def combination_sum(nums, target):
    lst = []
    res = []
    nums.sort()
    combination_helper(lst, nums, target, 0, res)
    return res


def combination_helper(lst, nums, remian, startindex, res):
    if remian == 0:
        res.append(lst[:])

    for i in range(startindex, len(nums)):
        if remian>0:
            lst.append(nums[i])
            combination_helper(lst, nums, remian - nums[i], i, res)
            lst.pop()


nums=[2,3,6,7]
target=7
print(combination_sum(nums,target))