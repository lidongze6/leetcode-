def find132pattern(nums):
    """
    记录从后到前的次最大值，注意是要求对当前元素之后的次大值
    :type nums: List[int]
    :rtype: bool
    """
    stack = []
    mid = float('-inf')  # 记录从后到前的次大值

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < mid:
            return True
        while stack and nums[i]>stack[-1]:
            mid = stack.pop()
        stack.append(nums[i])

    return False


nums = [3, 1, 4, 2]
print(find132pattern(nums))
