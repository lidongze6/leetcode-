def containsNearbyAlmostDuplicate(nums, k, t):
    if not nums or t < 0 or k < 0:
        return False
    w = t + 1
    c = {}
    for i in range(len(nums)):
        tmp = nums[i] // w
        if tmp not in c:
            c[tmp]=nums[i]
        else:
            return True
        if tmp - 1 in c and c[tmp - 1] and abs(c[tmp - 1] - nums[i]) <= t:
            return True
        if tmp + 1 in c and c[tmp + 1] and abs(c[tmp + 1] - nums[i]) <= t:
            return True
        if i >= k:
            c.pop(nums[i - k] // w)
    return False


nums = [1,5,9,1,5,9]
k = 2
t = 3
print(containsNearbyAlmostDuplicate(nums, k, t))
