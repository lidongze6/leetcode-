"""
给定一个整数数组，试写一个函数返回次枢纽的枢纽序号
枢纽序号的定义为：此元素左边所有元素之和与此元素右边所有元素之和相等
若不存在，则返回-1，存在多个，则返回最左边的序号
"""

def findmixNumber(nums):
    for i in range(0, len(nums)):
        left = sum(nums[0:i])
        right = sum(nums[i + 1:])
        if left==right:
            return i
    return -1

def findmixNumber1(nums):
    left=nums[0]
    right=sum(nums[2:])
    if left==right:return 1
    for i in range(2,len(nums)):
        left=left+nums[i-1]
        right=right-nums[i]
        if left==right:
            return i
    return -1


nums=[1,2,3,4,3,2,1]
print(findmixNumber(nums))
print(findmixNumber1(nums))