def search(nums, target):
    """
    主要是注意边界和当nums是完全升序时的情况
    这里要写成nums[mid]>nums[r]不能写成nums[mid]>=nums[l]就是为了防止nums是完全升序时的情况
    同理有nums[mid]<nums[l]不能写成nums[mid]<=nums[r]，
    以nums[mid]<target为例：当为完全升序时，nums[mid]必定<=nums[r]
    然而nums[mid]是<target的，因而应该调整l而不是r，这么写就是为了防止走r=mid-1这步而正确的走l=mid+1这步
    :param nums:
    :param target:
    :return:
    """
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            if target<=nums[r] and nums[mid]>nums[r]:
                l=mid+1
            else:r=mid-1
        else:
            if target>=nums[l] and nums[mid]<nums[l]:
                r=mid-1
            else:
                l=mid+1

    return -1

nums = [4,5,6,7,0,1,2]
target = 2
print(search(nums,target))