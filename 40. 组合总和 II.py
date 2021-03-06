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
        if nums[i]==nums[i-1] and i!=startindex:
            continue
        if remian>0:
            lst.append(nums[i])
            combination_helper(lst, nums, remian - nums[i], i+1, res)
            lst.pop()