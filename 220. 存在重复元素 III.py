def containsNearbyAlmostDuplicate(nums, k, t):
    if not nums or k == 0 or k == 10000:
        return False
    for i in range(len(nums) - 1):
        for j in range(i + 1, min(len(nums), i + k + 1)):
            if abs(nums[j] - nums[i]) <= t:
                return True
    return False

nums = [1,0,1,1]
k = 1
t = 2
print(containsNearbyAlmostDuplicate(nums,k,t))