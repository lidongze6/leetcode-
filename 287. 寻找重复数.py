def findDuplicate(nums) -> int:
    """
    循环检测法
    O(n)
    只要涉及到 "数都比数组长度小"的题
    都利用数组元素可以当数组index用的方法，把相应位置弄成负的
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        nextNum = nums[i]
        nums[i] = 0
        while nums[nextNum] != 0:
            temp = nums[nextNum]
            if temp == -1:
                return nextNum
            nums[nextNum] = -1
            nextNum = temp
    return -1



nums=[1,3,4,2,2]
print(findDuplicate(nums))