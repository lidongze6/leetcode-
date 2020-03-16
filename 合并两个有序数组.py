def merge(nums1, m, nums2, n):
    for i in range(m):
        if nums1[i] > nums2[0]:
            b = nums1[i]
            nums1[i] = nums2.pop(0)
            for j in range(n - 1):
                if b < nums2[j]:
                    nums2[j],b=b,nums2[j]
            nums2.append(b)
    nums1[m :m + n-1] = nums2
    return nums1



if __name__ == "__main__":
    nums1=[1, 2, 3, 0, 0, 0]
    m=3
    nums2=[2, 5, 6]
    n=3
    print(merge(nums1, m, nums2, n))