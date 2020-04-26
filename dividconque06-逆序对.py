"""
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。给你一个数组，求出这个数组中逆序对的总数。
概括：如果a[i] > a[j] 且 i < j， a[i] 和 a[j] 构成一个逆序对。
"""


def reversePairs(nums):
    if len(nums)==0 or len(nums)==1:
        return 0
    res = 0
    l, r = 0, len(nums) - 1

    def merge_helper(nums, l, r, res):
        if l >= r:
            return [nums[l]], 0
        mid = l + (r - l) // 2
        left, res_l = merge_helper(nums, l, mid, res)
        right, res_r = merge_helper(nums, mid + 1, r, res)

        tmp = []
        while left and right:
            if left[0] > right[0]:
                res += len(left)
                tmp.append(right.pop(0))
            elif left[0] <= right[0]:
                tmp.append(left.pop(0))

        tmp = tmp + left + right
        res = res + res_l + res_r
        return tmp, res

    _, res = merge_helper(nums, l, r, res)
    return res


nums = [1, 2, 3, 4]
print(reversePairs(nums))