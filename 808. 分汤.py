class Solution:
    def soupServings(self, N: int):
        if N % 25 == 0:
            N = N // 25
        else:
            N = N // 25 + 1

        f = [[0] * (N + 1) for _ in range(N + 1)]
        # f[i][j]为A-i升B-j升时的概率
        for i in range(N + 1):
            f[0][i] = 1
        f[0][0] = 0.5

        for i in range(1, N + 1):
            for j in range(1, N + 1):
                f[i][j] = 0.25 * (f[max(0,i - 4)][j] + f[max(0,i - 3)][max(0,j - 1)] + f[max(i - 2,0)][max(0,j - 2)] + f[max(0,i - 1)][max(j - 3,0)])
        return f[N][N]


