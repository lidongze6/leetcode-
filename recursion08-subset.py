def subset(nums):
    lst = []
    res = []
    subset_helper(res, lst, nums, 0)
    return res


def subset_helper(res,lst,nums,po):
    res.append(lst[:])
    for i in range(po,len(nums)):
        lst.append(nums[i])
        subset_helper(res,lst,nums,i+1)
        lst.pop()


nums = ["a", "b", "c"]
print(subset(nums))
