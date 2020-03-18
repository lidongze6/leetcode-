class Solution:
    def rob(self, nums) -> int:
        # DP：time：O(n) space:O(1)
        # Y[n]=N[n-1]+nums[n]
        # N[n]=max(Y[n-1],N[n-1])
        # res=max(Y[n],N[n])
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        Y=nums[0]
        N=0
        for i in range(1,len(nums)):
            Y,N=N+nums[i],max(Y,N)
        return max(Y,N)