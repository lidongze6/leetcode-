class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
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