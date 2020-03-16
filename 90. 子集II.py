"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集
"""


def subset(nums):
    nums.sort()
    lst = []
    res = []
    subset_helper(lst, nums, 0, res)
    return res

def subset_helper(lst, nums, startindex, res):
    res.append(lst[:])

    for i in range(startindex, len(nums)):
        if i > 0 and nums[i] == nums[i - 1] and i != startindex:
            # nums[i]==nums[i-1] and i !=startindex 防止跳过第一个2直接选择第二个2，而[1,2,2]这样的是可以的
            continue
        lst.append(nums[i])
        subset_helper(lst, nums, i + 1, res)
        lst.pop()


nums = [1, 2, 2]
print(subset(nums))
