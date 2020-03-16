def quick_select(nums, k):
    # 改进的快排
    l,r=0,len(nums)-1
    while 1:
        mid = select_helper(nums, l, r)
        if mid == len(nums) - k:
            return nums[mid]
        elif mid > len(nums) - k:
            r=mid-1
        else:
            l=mid+1


def select_helper(nums, start, end):
    if start >= end:
        return start
    l, r = start, end
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]

        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    return l


nums = [7, 6, 5, 4, 3, 2, 1]
k = 5
print(quick_select(nums, k))
