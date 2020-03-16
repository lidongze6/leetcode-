def counting_sort(nums):
    if not nums or len(nums)==1:
        return nums

    m=min(nums)
    k=max(nums)-m
    c=[0 for _ in range(k+1)]
    res=[]

    for i in nums:
        c[i-m]+=1
    for n in range(len(c)):
        res=res+[n+m]*c[n]

    return res


nums=[21,3,45,130,77,71,25,86,60,101,103]
print(counting_sort(nums))
