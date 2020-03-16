def sortColors(nums):
    """
    计数排序，遍历两趟
    """
    if not nums:return
    k=max(nums)
    c=[0 for _ in range(k+1)]
    res=[0 for _ in range(len(nums))]
    for i in nums:
        c[i]+=1
    for j in range(1,len(c)):
        c[j]+=c[j-1]
    for n in nums:
        res[c[n]-1]=n
        c[n]-=1
    return res

nums=[2,0,2,1,1,0]
print(sortColors(nums))
print(nums)

