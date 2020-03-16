"""
无限序列中找某元素第一次出现的位置
无限序列：即len（nums）=无穷大
"""
def findfirstnumsinSteam(nums,target):
    l,r=0,1
    while nums[r]<target:
        l=r
        r*=2

    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            r=mid
        elif nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
    if nums[l]==target:
        return l
    if nums[r]==target:
        return r
    else:return -1



nums=[1,1,1,2,2,2,3,3,3,3,3,3,3,4,4,5,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,10,11]
print(findfirstnumsinSteam(nums,6))