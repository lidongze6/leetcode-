"""
给定一个数组，返回+1后的数组
"""
def Pluse_One(nums):
    ad=True
    for i in range(len(nums)-1,0,-1):
        if nums[i]==9 and ad==True:
            nums[i]=0
        else:
            nums[i]+=1
            ad=False
            break
    if ad==True:
        if nums[0]==9:
            nums[0]=0
            nums.insert(0,1)
        else:
            nums[0]+=1
    return nums

def Pluse_One2(nums):
    if len(nums)==0:
        return False
    ad=1
    for i in range(len(nums)-1,-1,-1):
        nums[i]+=ad
        if nums[i]==10:
            nums[i]=0
            if i==0:
                nums.insert(0,1)
        else:
            break
    return nums

nums=[3,9,9]
print(Pluse_One(nums))
print(Pluse_One2(nums))