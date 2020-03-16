def containsNearbyDuplicate(nums, k):
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] not in dict1:
            dict1[nums[i]] = i
        else:
            if i - dict1[nums[i]] <= k:
                return True
            else:
                dict1[nums[i]] = i
    return False
