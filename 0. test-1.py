class Solution:
    def bestSeqAtIndex(self, height, weight) -> int:
        hw = [[height[i], weight[i]] for i in range(len(height))]
        hw.sort(key=lambda x: x[0])
        res = [hw[0][1]]
        for i in range(1, len(height)):
            pos = self.binarysearch(res, hw[i][1])
            if pos == len(res):
                res.append(hw[i][1])
            else:
                res[pos] = hw[i][1]

        return len(res)

    def binarysearch(self, nums, tar):
        # [1,3,10,14,20]
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > tar:
                r = mid
            else:
                l = mid + 1
        if nums[l] < tar < nums[r]: return r
        if nums[r] < tar: return r + 1
        if tar < nums[l]: return l


height = [65, 70, 56, 75, 60, 68]

weight = [100, 150, 90, 190, 95, 110]
print(Solution().bestSeqAtIndex(height, weight))
