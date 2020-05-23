class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        # 坐标型DP，方法和前缀和类似
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        # dp[i][j][0]表示grid[i][j]左边的连续为1的个数
        # dp[i][j][1]表示grid[i][j]上边的连续为1的个数
        dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 1:
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1

                    d = min(dp[i][j])
                    while d > res:
                        if dp[i][j - d + 1][1] >= d and dp[i - d + 1][j][0] >= d:
                            res = d
                        d -= 1
        return res ** 2
