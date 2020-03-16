def majorityElement(nums):
    # 分治:O(nlogn)
    l,r=0,len(nums)-1
    def helper(nums,l,r):
        if l>=r:
            return nums[l]
        mid=l+(r-l)//2
        left_num=helper(nums,l,mid)
        right_num=helper(nums,mid+1,r)
        if right_num==left_num:
            return left_num

        else:
            left_count=sum(1 for i in range(l,r+1) if nums[i]==left_num)
            right_count=sum(1 for i in range(l,r+1) if nums[i]==right_num)
            return left_num if left_count>right_count else right_num
    return helper(nums,l,r)

nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))