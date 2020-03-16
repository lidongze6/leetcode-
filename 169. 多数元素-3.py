def majorityElement(nums):
    # 摩尔投票法 O(n)
    res, count = None, 0
    for i in nums:
        if count == 0:
            res = i
            count += 1
        elif count != 0:
            if i == res:
                count += 1
            else:
                count -= 1
    return res
