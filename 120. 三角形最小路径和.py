class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #坐标型DP
        if len(triangle)==1:
            return triangle[0][0]
        f=[[0 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        f[0][0]=triangle[0][0]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i==0 and j==0:
                    continue
                elif j==0:
                    f[i][j]=f[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    f[i][j]=f[i-1][j-1]+triangle[i][j]
                else:
                    f[i][j]=min(f[i-1][j],f[i-1][j-1])+triangle[i][j]
        return min(f[len(triangle)-1])