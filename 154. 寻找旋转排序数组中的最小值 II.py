def findMin(nums):
    if len(nums)==1:
        return nums[0]
    l,r=0,len(nums)-1
    while l+1<r:
        if nums[l]<nums[r]:
            return nums[l]
        mid=l+(r-l)//2
        if nums[mid]==nums[l]==nums[r]:
            l+=1
            r-=1
        elif nums[mid]>=nums[l]:
            l=mid
        elif nums[mid]<=nums[r]:
            r=mid
    return nums[l] if nums[l]<=nums[r] else nums[r]


nums=[10,1,10,10,10]
print(findMin(nums))
