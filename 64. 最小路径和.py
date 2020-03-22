class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 坐标型DP
        row, col = len(grid), len(grid[0])
        f = [[0] * col for i in range(row)]
        f[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i][j - 1] + grid[i][j], f[i - 1][j] + grid[i][j])

        return f[row - 1][col - 1]