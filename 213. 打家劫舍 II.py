class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # if 抢第一家，则最后一家不能抢，相当于计算nums[0:n-1]
        # if 不抢抢第一家，则最后一家可以抢，相当于计算nums[1:n]
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        def helper(start, end):
            Y = nums[start]
            N = 0
            for i in range(start + 1, end):
                Y, N = N + nums[i], max(Y, N)
            return max(Y, N)

        return max(helper(0, len(nums) - 1), helper(1, len(nums)))
