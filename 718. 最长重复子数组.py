class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        f=[[0]*(len(B)+1) for i in range((len(A)+1))]
        # f[i][j] 表示以i，j结尾的子数组的最长公共子数组
        res=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    f[i][j]=f[i-1][j-1]+1
                    res=max(res,f[i][j])

        return res
