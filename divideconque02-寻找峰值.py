def findpeaknum(nums):
    """
    nums：无序数组且首位值nums[0],nums[-1]为去穷小
    return:返回任意峰值即可
    """
    l,r=0,len(nums)-1
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
            return mid
        elif nums[mid-1]<=nums[mid]<=nums[mid+1]:
            l=mid+1
        elif nums[mid-1]>=nums[mid]:
            r=mid-1
    if nums[r]<nums[l] and nums[l]>nums[l-1]:
        return l
    if nums[r]>nums[l] and nums[r]>nums[r+1]:
        return r
    return -1 