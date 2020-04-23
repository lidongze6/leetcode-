class Solution:
    def dieSimulator(self, n: int, rollMax) -> int:
        f = [[[0] * 16 for i in range(7)] for j in range(n + 1)]
        # f[i][j][k] 表示掷了第i此是j点且是连续掷出第k此的方法数
        MOD = 10 ** 9 + 7
        for j in range(1, 7):
            f[1][j][1] = 1

        for i in range(1, n + 1):
            for j in range(1, 7):  # 第i此掷出j点
                for m in range(1, 7):  # 第i-1此掷出m点
                    if j == m:
                        for k in range(2, rollMax[j - 1] + 1):
                            f[i][j][k] = f[i - 1][j][k - 1]
                    else:
                        f[i][j][1] += sum(f[i - 1][m]) % MOD

        ans = [0, 0, 0, 0, 0, 0, 0]
        for j in range(1, 7):
            ans[j] = sum(f[-1][j]) % MOD
        return sum(ans) % MOD
