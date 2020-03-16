def findMaxLength(nums):
    list1 = [-1 if i == 0 else 1 for i in nums]
    # 构造前缀和
    pre_sum = [0] * (len(list1) + 1)
    for i in range(1, len(pre_sum)):
        pre_sum[i] = pre_sum[i - 1] + list1[i - 1]

    dict1 = dict()
    res = 0
    for n, num in enumerate(pre_sum):
        if num not in dict1:
            dict1[num] = n
        else:
            res = max(res, n - dict1[num])
    return res


nums = [0, 1, 1]
print(findMaxLength(nums))
