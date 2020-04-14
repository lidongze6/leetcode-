class Solution:
    def minScoreTriangulation(self, A) -> int:
        # DFS+记忆化
        dic=dict()
        def dfs(nums):
            if len(nums)<=2:return 0
            if len(nums)==3:return nums[0]*nums[1]*nums[2]
            if tuple(nums) in dic:
                return dic[tuple(nums)]
            else:
                res=float("inf")
                for i in range(1,len(nums)-1):
                    res=min(res,dfs(nums[:i+1])+dfs(nums[i:len(nums)])+nums[0]*nums[-1]*nums[i])
                    dic[tuple(nums)]=res

                return res

        return dfs(A)
