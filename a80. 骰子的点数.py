class Solution(object):
    def numberOfDice(self, n):
        if n == 1: return [1, 1, 1, 1, 1, 1]
        f = [[0] * (1 + 6 * n) for i in range(1 + n)]

        f[0][0] = 1
        for i in range(1, 7):
            f[1][i] = 1

        for i in range(2, 1 + n):
            for j in range(i, 6 * i + 1):
                for k in range(1, 7):
                    f[i][j] += f[i - 1][j - k]

        return f[n][n:]

print(Solution().numberOfDice(2))
