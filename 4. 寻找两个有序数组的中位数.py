def findMedianSortedArrays(nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2 == 1:
        return helper(nums1, nums2, l // 2 + 1)
    else:
        return (helper(nums1, nums2, l // 2 + 1) + helper(nums1, nums2, l // 2)) / 2


def helper(nums1, nums2, k):
    # 始终保持nums1是短的，简化代码
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Base 若是剩下数组的第一小的数，则返回两个已排序数组中首元素最小的那个
    if k == 1 and nums1 and nums2:
        return nums1[0] if nums1[0] <= nums2[0] else nums2[0]

    # 若其中一组为空了，则直接返回另一组的第k个小的数即是所求
    if not nums1:
        return nums2[k - 1]

    mid = k // 2
    l1 = l2 = 0
    if len(nums1) >= mid and len(nums2) >= mid:
        if nums1[mid - 1] <= nums2[mid - 1]:
            l1 = mid
        else:
            l2 = mid
        return helper(nums1[l1:], nums2[l2:], k - mid)

    elif len(nums1) < mid:
        if nums1[-1] <= nums2[mid - 1]:
            return nums2[k - len(nums1) - 1]
        else:
            l2 = mid
            return helper(nums1, nums2[l2:], k - mid)


nums1 = [4]
nums2 = [1, 2, 3, 5, 6]
print(findMedianSortedArrays(nums1, nums2))
