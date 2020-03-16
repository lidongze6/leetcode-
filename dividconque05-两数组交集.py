def intersection(nums1, nums2):
    # O(n2)
    res=set()
    for i in nums1:
        for j in nums2:
            if i==j:
                res.add(i)

def intersection_2(nums1,nums2):
    # O((n+m)logn)
    nums1.sort()
    nums2.sort()
    res=set()
    def find_helper(nums,target):
        if nums==[]:return False
        l,r=0,len(nums2)-1
        while l+1<r:
            mid=l+(r-l)//2
            if nums2[mid]==target:
                return True
            elif nums2[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return True if (nums2[l]==target or nums2[r]==target) else False
    for i in nums1:
        tmp=find_helper(nums2,i)
        if tmp:
            res.add(i)
    return res

def intersection_3(nums1,nums2):
    # O(nlogn)
    nums1.sort()
    nums2.sort()
    l1,l2=0,0
    res=set()
    while l1<len(nums1) and l2<len(nums2):
        if nums1[l1]==nums2[l2]:
            res.add(nums1[l1])
            l1+=1
            l2+=1
        elif nums1[l1]<nums2[l2]:
            l1+=1
        elif nums1[l1]>nums2[l2]:
            l2+=1
    return res

nums1=[4,9,5]
nums2=[9,4,9,8,4]
print(intersection_3(nums1,nums2))