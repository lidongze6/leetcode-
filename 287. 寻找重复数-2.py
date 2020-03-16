def findDuplicate(nums):
    """
    数值二分法
    O(NlogN)
    只需判断数组中不超过中间数 m 的元素数量是否大于 m 即可，若大于，则表示范围 1 到 m 内肯定包含重复的数字
    :param nums:
    :return:
    """
    l,r=1,len(nums)-1
    while l<r:
        count=0
        mid=(l+r)//2
        for i in nums:
            if i<=mid:
                count+=1
        if count<=mid:
            l=mid+1
        else:r=mid
    if l>=r:
        return l

nums=[3,1,3,4,2]
print(findDuplicate(nums))