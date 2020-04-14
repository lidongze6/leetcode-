class Solution:
    def minScoreTriangulation(self, A):
        l=len(A)
        if l==3:return A[0]*A[1]*A[2]
        f=[[float("inf")]*l for i in range(l)]
        # f[i][j] 从i到j角点的三角形乘积最小和

        for i in range(1,l):
            f[i-1][i]=0

        for k in range(2,l):
            for i in range(l-k):
                j=i+k
                for m in range(i+1,j):
                    f[i][j]=min(f[i][j],f[i][m]+A[i]*A[j]*A[m]+f[m][j])
        return f[0][l-1]