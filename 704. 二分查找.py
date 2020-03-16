def search(nums, target):
    l,r=0,len(nums)-1
    while l<r:
        mid=l+(r-l)//2
        if nums[mid]>target:
            r=mid-1
        elif nums[mid]<target:
            l=mid+1
        else: return mid

    if l>=r:
        if nums[l] !=target:
            return -1
        else:
            return l


nums=[-1,0,3,5,9,12]
target=9
print(search(nums,target))