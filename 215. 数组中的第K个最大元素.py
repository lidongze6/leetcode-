def findKthLargest(nums, k):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = select_helper(nums, l, r)
        if len(nums[mid:r + 1]) == k:
            return nums[mid]
        elif len(nums[mid:r + 1]) > k:
            l = mid + 1
        elif len(nums[:mid + 1]) > k:
            k = k - len(nums[mid:r + 1])
            r = mid - 1
    if k == 1:
        return nums[l] if nums[l] >= nums[r] else nums[r]
    if k == 2:
        return nums[l] if nums[l] < nums[r] else nums[r]


def select_helper(nums, start, end):
    if start >= end:
        return
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


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))
