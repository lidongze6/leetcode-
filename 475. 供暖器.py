def findRadius(houses,heaters):
    radius=[None]*len(houses)
    heaters.sort()

    def findmin(nums,target):
        l,r=0,len(nums)-1
        while l+1<r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return 0
            elif nums[mid]>target:
                r=mid
            elif nums[mid]<target:
                l=mid
        if nums[l]==target or nums[r]==target:
            return 0
        elif nums[l]<target<nums[r]:
            return min(nums[r]-target,target-nums[l])
        elif nums[l]>target:
            return  min(nums[l]-target,target-nums[l-1]) if l>0 else nums[l]-target
        elif nums[r]<target:
            return min(target-nums[r],nums[r+1]-target) if r<len(nums)-1 else target-nums[r]

    for i in range(len(houses)):
        radius[i]=findmin(heaters,houses[i])
    return max(radius)

houses=[1,2,3]
heaters=[2]
print(findRadius(houses,heaters))