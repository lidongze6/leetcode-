def maxSubArray(nums):
    # O(n2)
    if nums == []:
        return None
    elif len(nums) == 1:
        return nums[0]
    max_sum = "-inf"
    for i in range(len(nums)):
        if nums[i]>=0:
            local_sum = 0
            j = i
            while j < len(nums):
                local_sum += nums[j]
                if local_sum > float(max_sum):
                    max_sum = local_sum
                j+=1
    return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))