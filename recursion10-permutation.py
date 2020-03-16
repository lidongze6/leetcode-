def permute(nums):
    nums.sort()
    lst=[]
    res=[]
    permute_helper(nums,lst,res)
    return res


def permute_helper(nums,lst,res):
    if len(nums)==0:
        res.append(lst[:])
    for i in range(len(nums)):
        lst.append(nums[i])
        permute_helper(nums[:i]+nums[i+1:],lst,res)
        lst.pop()

nums=[1,2,3]
print(permute(nums))