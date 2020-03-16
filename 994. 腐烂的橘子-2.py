class Solution:
    def orangesRotting(self, grid):
        from collections import deque
        if not grid: return 0
        stack = deque()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    stack.append([i, j])
        time = 0
        while stack:
            next_stack = deque()
            for _ in range(len(stack)):
                x, y = stack.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= dx + x < row and 0 <= dy + y < col and grid[dx + x][dy + y] == 1:
                        grid[dx + x][dy + y] = 2
                        next_stack.append([dx + x, dy + y])
            if not next_stack:
                break
            stack = next_stack
            time += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time


grid = [[2, 2],
        [1, 1],
        [0, 0],
        [2, 0]]
s = Solution()
print(s.orangesRotting(grid))
