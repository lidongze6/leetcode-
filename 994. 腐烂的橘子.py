class Solution:
    def orangesRotting(self, grid):
        from collections import deque
        if not grid: return 0
        stack = deque()
        row, col = len(grid), len(grid[0])
        visit = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))
                if grid[i][j] == 1:
                    visit.add((i, j))
        if len(visit) == 0: return 0

        while stack:
            x, y, time = stack.popleft()
            if (x, y) in visit:
                visit.remove((x, y))
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < row and 0 <= y + dy < col and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    stack.append((x + dx, y + dy, time + 1))

        return time if len(visit) == 0 else -1


grid = [[2, 2],
        [1, 1],
        [0, 0],
        [2, 0]]
s = Solution()
print(s.orangesRotting(grid))
