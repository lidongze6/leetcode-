class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # DP
        f = [[[0] * n for i in range(m)] for j in range(N+1)]
        # f[k][i][j] 表示 第k步走到位置[i][j]出界的方法数

        for k in range(1, N+1):
            for i in range(m):
                for j in range(n):
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if i + dx < 0 or i + dx >= N or j + dy < 0 or j + dy >= N:
                            f[i][j][k] += 1
                        else:
                            f[i][j][k] += f[i + dx][j + dy][k - 1]
        return f[m-1][n-1][k]


m = 3
n = 3
N = 2
i = 0
j = 0
print(Solution().findPaths(m,n,N,i,j))