def check():
    return


## 当求右边界时使用，此时区间[l, r]被划分成[l, mid]和[mid + 1, r]：
def bsearch_r(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid
        elif nums[mid] == target:
            l = mid
    if nums[r] == target:
        return r
    elif nums[l] == target:
        return l
    return -1


## 当求左边界时使用，此时区间[l, r]被划分成[l, mid]和[mid + 1, r]：
def bsearch_l(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        elif nums[mid] == target:
            r = mid
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    return -1


nums = [17, 20, 26, 29, 31, 32, 34, 44, 44, 54, 55, 56, 77, 93, 103, 123]
print(bsearch_l(nums, 44))
print(bsearch_r(nums, 44))
