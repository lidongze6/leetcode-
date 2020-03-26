class Solution:
    def surfaceArea(self, grid) -> int:
        surfaceSum = 0
        N = len(grid)
        for i in range(N):
            # 一排一排算
            surfaceSum += sum([4 * n + 2 if n > 0 else 0 for n in grid[i]])
            # 层间重叠
            stack = 2 * sum([min(grid[i][j], grid[i][j - 1]) for j in range(1, N)])
            surfaceSum -= stack
            # 再中间减去和前一排的重叠部分
            if i > 0:
                stack = 2 * sum([min(grid[i - 1][j], grid[i][j]) for j in range(N)])
                surfaceSum -= stack
        return surfaceSum
