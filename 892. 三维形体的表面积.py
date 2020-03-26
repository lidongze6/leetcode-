class Solution:
    def surfaceArea(self, grid) -> int:
        if not grid: return 0
        sum_res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    sum_res += (grid[i][j] * 4 + 2)

        diff_res = 0

        def bfs():
            nonlocal diff_res
            from collections import deque
            stack = deque()
            stack.append((0, 0))
            visit = set()
            while stack:
                x, y = stack.popleft()
                for dx, dy in [[1, 0], [0, 1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        diff_res += min(grid[x][y], grid[x + dx][y + dy]) * 2
                        if (x + dx, y + dy) not in visit:
                            stack.append((x + dx, y + dy))
                            visit.add((x + dx, y + dy))

        bfs()
        return sum_res - diff_res


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

print(Solution().surfaceArea(grid))
