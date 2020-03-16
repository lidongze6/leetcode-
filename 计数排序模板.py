def counting_sort(nums):
    if not nums or len(nums)==1:
        return nums

    m=min(nums)
    k=max(nums)-m
    c=[0 for _ in range(k+1)]
    res=[]

    for i in nums:
        c[i-m]+=1
    for j in range(len(c)):
        res=res+[j+m]*c[j]
    return res


nums=[21,3,5,20,19,2,5,21,5,8]
print(counting_sort(nums))
