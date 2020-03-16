"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""


def combine(n, k):
    nums = [i for i in range(1, n + 1)]
    if n < k:
        return []
    elif n == k:
        return [nums]
    lst = []
    res = []
    combine_helper(lst, res, nums, k, 0)
    return res


def combine_helper(lst, res, nums, k_remain, starrindex):
    if k_remain == 0:
        res.append(lst[:])
        return
    for i in range(starrindex, len(nums)):
        lst.append(nums[i])
        combine_helper(lst, res, nums, k_remain - 1, i + 1)
        lst.pop()


print(combine(4, 2))
