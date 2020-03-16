def twoSum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        if target - nums[i] in dict1:
            return [i, dict1[target - nums[i]]]
        else:
            dict1[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
