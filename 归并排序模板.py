def mergesort(nums, start, end):
    if start >= end: return
    mid = (start + end) // 2
    mergesort(nums, start, mid)
    mergesort(nums, mid + 1, end)

    return merge(nums, start, end)


def merge(nums, start, end):
    mid = (start + end) // 2
    lindex, rindex = start, mid + 1
    tmp = []
    while lindex <= mid and rindex <= end:
        if nums[lindex] < nums[rindex]:
            tmp.append(nums[lindex])
            lindex += 1
        else:
            tmp.append(nums[rindex])
            rindex += 1
    if lindex <= mid:
        tmp += nums[lindex:mid + 1]
    elif rindex <= end:
        tmp += nums[rindex:end + 1]
    nums[start:end + 1] = tmp
    return


nums = [21, 3, 45, 130, 77, 71, 25, 86, 60, 101, 103]
start, end = 0, len(nums) - 1
mergesort(nums, start, end)
print(nums)
