class Solution:
    def massage(self, nums: List[int]) -> int:
        Y=nums[0]
        N=0
        for i in range(1,len(nums)):
            Y,N=N+nums[i],max(Y,N)
        return max(Y,N)