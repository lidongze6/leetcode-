class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 坐标型DP，有障碍则f[i][j]直接赋值为0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1: return 0
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    if i > 0:
                        f[i][j] += f[i - 1][j]
                    if j > 0:
                        f[i][j] += f[i][j - 1]
        return f[m - 1][n - 1]
