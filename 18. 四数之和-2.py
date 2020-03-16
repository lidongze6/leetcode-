def fourSum(nums, target):
    res = []
    if len(nums) < 4:
        return None
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        elif len(nums[i:]) >= 4:
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                elif len(nums[j:]) >= 3 :
                    remain = target - nums[i] - nums[j]
                    left = j + 1
                    right = len(nums) - 1
                    while left < right:
                        if nums[left] + nums[right] > remain:
                            right -= 1
                        elif nums[left] + nums[right] < remain:
                            left += 1
                        else:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                            while nums[left] == nums[left - 1] and left<right:
                                left+=1
                            while nums[right] == nums[right + 1] and left < right:
                                right -= 1
    return res

nums = [-3,-2,-1,0,0,1,2,3]
target=0
print(fourSum(nums,target))