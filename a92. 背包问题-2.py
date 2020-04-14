class Solution:
    def backPack(self, m, A):
        l = len(A)
        f = [[0] * (m + 1) for i in range(l + 1)]

        for i in range(1, l + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if j - A[i - 1] >= 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - A[i - 1]] + A[i - 1])

        return f[-1][-1]