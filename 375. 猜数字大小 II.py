class Solution:
    def getMoneyAmount(self, n: int):
        # 区间型DP f[i][j]=min(f[i][j],max(f[i][k-1]+k,f[k+1][j]+k) for k in (i+1,j)
        if n == 1: return 0
        f = [[float("inf")] * (n + 1) for i in range(n + 1)]  # f[i][j] 表示数字i-j最少需要f[i][j]元钱

        # 求f[1][n]
        for i in range(1, n):  # 8-9至少需要8元钱
            f[i][i + 1] = i
        for i in range(1,n+1):
            f[i][i]=0
        for len in range(2, n):
            for i in range(1, n + 1):
                j = i + len
                if j >=n + 1:
                    break
                for k in range(i+1, j):
                    f[i][j] = min(f[i][j], max(f[i][k - 1] + k, f[k + 1][j] + k))

        return f[1][n]


n = 4
print(Solution().getMoneyAmount(n))
