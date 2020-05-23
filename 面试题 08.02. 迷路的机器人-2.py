class Solution:
    def pathWithObstacles(self, obstacleGrid):
        # DP
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[float("inf")] * n for i in range(m)]
        # -1走不动，1向下，2向右
        pi = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    pi[i][j] = -1
                    continue
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 0
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1] + 1
                        pi[i][j] = 2
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j] + 1
                        pi[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                        if dp[i][j] == dp[i - 1][j] + 1:
                            pi[i][j] = 1
                        elif dp[i][j] == dp[i][j - 1] + 1:
                            pi[i][j] = 2
        p, q = m - 1, n - 1
        res = []
        while p != 0 or q != 0:
            res.append([p, q])
            if pi[p][q] == 1:
                p -= 1
            elif pi[p][q] == 2:
                q -= 1
        res.append([p, q])
        return res[::-1]


obstacleGrid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
print(Solution().pathWithObstacles(obstacleGrid))
