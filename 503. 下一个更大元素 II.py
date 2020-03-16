def nextGreaterElements(nums):

    """
    其实就是相当于现将原始数组的倒叙添加到栈里面
    这样是为了对于后面的尤其是倒数的几个数在判断时候可以有值而不是先为-1
    :param nums:
    :return:
    """
    stack = nums[::-1]
    right_large=[-1 for _ in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack and stack[-1] > nums[i]:
            right_large[i] = stack[-1]
        stack.append(nums[i])
    return right_large



nums = [100,1,11,1,120,111,123,1,-1,-100]
print(nextGreaterElements(nums))

