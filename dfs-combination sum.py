def combination_sum(nums,target):
    if nums==[] or nums==None:
        return None
    lst=[]
    res=[]
    # 把所有以[]开头的和为target的组合放到res里面
    recursion_help(nums,0,target,lst,res)
    return res

def recursion_help(nums,po,remian,lst,res):
    if remian==0:
        res.append(lst[:])
        return
v
    for i in range(po,len(nums)):
        if remian<nums[i]:
            break
        if i !=0 and nums[i]==nums[i-1]:
            continue
        lst.append(nums[i])
        recursion_help(nums,i,remian-nums[i],lst,res)
        lst.pop()


nums=[2,2,3,6,7]
target=7
print(combination_sum(nums,target))