class Solution:
    def minFallingPathSum(self, A) -> int:
        m, n = len(A), len(A[0])
        f = [[0] * n for i in range(m)]
        for i in range(n):
            f[0][i] = A[0][i]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    f[i][j] = min(f[i - 1][j], f[i - 1][j + 1]) + A[i][j]
                elif j == n - 1:
                    f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + A[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i - 1][j - 1], f[i - 1][j + 1]) + A[i][j]

        return min(f[-1])

A=[[1,2,3],[4,5,6],[7,8,9]]
print(Solution().minFallingPathSum(A))