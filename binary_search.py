def binary_search(nums,target):
    l,r=0,len(nums)-1
    while l+1<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            r=mid-1
        elif nums[mid]<target:
            l=mid+1
    if nums[l]==target:
        return l
    if nums[r]==target:
        return r
    else:
        return -1

if __name__ == "__main__":
    li = [17, 20, 26, 29, 31, 32, 34, 44, 54, 55, 56, 77, 93, 103, 123]
    target=123
    print(binary_search(li, target))
