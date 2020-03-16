def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []

    def find_helper(nums, l, target):
        if nums == []: return -1
        r = len(nums) - 1
        if l>r:return -1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        else:
            return -1

    l=0
    for i in nums1:
        tmp = find_helper(nums2, l, i)
        if tmp != -1:
            res.append(nums2[tmp])
            l=tmp+1
    return res



def intersection_2(nums1,nums2):
    # two points
    nums1.sort()
    nums2.sort()
    l1=l2=0
    res=[]
    while l1<len(nums1) and l2<len(nums2):
        if nums1[l1]==nums2[l2]:
          res.append(nums1[l1])
          l1+=1
          l2+=1
        elif nums1[l1]<nums2[l2]:
            l1+=1
        elif nums1[l1]>nums2[l2]:
            l2+=1
    return res

nums1 = [1, 2, 2, 1]
nums2 = [1, 2,2]
print(intersection(nums1, nums2))
