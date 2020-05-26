class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1)
        k = (len(nums1) + len(nums2) + 1) // 2
        while l + 1 < r:
            i = l + (r - l) // 2
            j = k - i
            if nums1[i - 1] > nums2[j]:
                r = i - 1
            else:
                l = i
        if nums1[l - 1] <= nums2[k - l]:
            tmp = l+1
        elif nums1[r - 1] <= nums2[k - r]:
            tmp = r + 1
        num1leftmax=
#TODO

nums1 = [4]
nums2 = [1, 2, 3, 5, 6]
print(Solution().findMedianSortedArrays(nums1, nums2))
