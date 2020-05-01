class Solution:
    def countSquares(self, matrix) -> int:
        # 同leetcode221
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res += dp[i][j]
        return res
