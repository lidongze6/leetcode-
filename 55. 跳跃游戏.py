class Solution:
    def canJump(self, nums) -> bool:
        l=len(nums)
        if l<=1:return True
        f=[False]*(l)

        f[0]=True
        for i in range(1,l):
            for j in range(i):
                if f[j] and j+nums[j]>=i:
                    f[i]=True
                    break

        return f[l-1]