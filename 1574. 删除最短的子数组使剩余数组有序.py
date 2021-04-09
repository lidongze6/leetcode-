class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 本题搜索的上升区间有三种可能
        # 1、arr[:left] left为从左端点能达到的最长上升区间
        # 2、arr[right:] right为到达右端点能达到的最长上升区间
        # 3、arr[:left]的一部分+arr[right:]的一部分，这部分就需要查找arr[:left]中的值在arr[right:]中能插入的位置
        # 删除的元素几位这之间的元素
        left, right = 0, len(arr) - 1
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                left = i
            else:
                break
        if left == len(arr) - 1:
            return 0

        for j in range(len(arr) - 2, -1, -1):
            if arr[j] <= arr[j + 1]:
                right = j
            else:
                break

        res = min(len(arr) - left - 1, right)

        nums = arr[right:]

        for k in range(left, -1, -1):
            index = self.binary_search(nums, arr[k])
            res = min(res, right - 1 - k + index)
        return res

    def binary_search(self, nums, target):
        # 35题解
        # 注意：这里插入位置，要求是最左边第一个大于等于它的元素位置，故必须有下面的判断，否则会出错
        # 例：[1,2,3,5]插入6 ，要是没有下面的判断会返回index=4
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
