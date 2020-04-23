class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == "1":
                        stack.append((x + dx, y + dy))
                        grid[x + dx][y + dy] = "0"
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i, j)
                    count += 1
        return count


grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
