def choosesort(nums):
    if not nums or len(nums)==1:
        return nums

    l=len(nums)
    for i in range(l):
        tmp=i
        for j in range(i,l):
            if nums[j]<nums[tmp]:
                tmp=j
        nums[i],nums[tmp]=nums[tmp],nums[i]


nums = [21, 3, 45, 130, 77, 71, 25, 86, 60, 101, 103]
choosesort(nums)
print(nums)


