def maxSlidingWindow(nums, k):
    from collections import deque
    queue = deque()
    res = []

    for i in range(len(nums)):
        if queue and i - queue[0] + 1 > k:  # 保证queue内的元素在k个以内
            queue.popleft()

        while queue and nums[queue[-1]] <= nums[i]:  # 维护一个单调递减队列
            queue.pop()

        queue.append(i)
        if i + 1 - k >= 0:  # 保证从第k个数开始输出
            res.append(nums[queue[0]])
    return res


nums = [1,3,-1,-3,5,3,6,7]
print(maxSlidingWindow(nums,3))