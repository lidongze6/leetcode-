## 当求右边界时使用，此时区间[l, r]被划分成[l, mid]和[mid + 1, r]：
def bsearch_r(nums, target, l, r):
    if l + 1 >= r:
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        else:
            return -1
    mid = l + (r - l) // 2
    if nums[mid] > target:
        return bsearch_r(nums, target, l, mid)
    elif nums[mid] <= target:
        return bsearch_r(nums, target, mid, r)


## 当求左边界时使用，此时区间[l, r]被划分成[l, mid]和[mid + 1, r]：
def bsearch_l(nums, target, l, r):
    if l + 1 >= r:
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        else:
            return -1
    mid = l + (r - l) // 2
    if nums[mid] >= target:
        return bsearch_l(nums, target, l, mid)
    elif nums[mid] < target:
        return bsearch_l(nums, target, mid, r)


nums = [17, 20, 26, 29, 31, 32, 34, 44, 44, 54, 55, 56, 77, 93, 103, 123]
print(bsearch_l(nums, 44, 0, len(nums)))
print(bsearch_r(nums, 44, 0, len(nums)))
