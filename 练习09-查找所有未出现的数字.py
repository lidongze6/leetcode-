def findDispearnumbers(nums):
    """
    给一个n个数的数组，范围为1-n
    里面有的数字重复多次，有的数字没出现过，找到所有未出现的数字
    """
    # 因为n个数字范围在1-n，故可以考虑使用计数排序的思想就是用index记录数字
    index = []
    for i in nums:
        if nums[abs(i) - 1] >= 0:
            nums[abs(i) - 1] = -1 * nums[abs(i) - 1]
    for j in range(len(nums)):
        if nums[j] > 0:
            index.append(j + 1)

    return index


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDispearnumbers(nums))
