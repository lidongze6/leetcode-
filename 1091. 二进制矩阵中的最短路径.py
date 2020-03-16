class Solution:
    def shortestPathBinaryMatrix(self, grid):
        from collections import deque
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1: return -1
        visit = set()
        stack = deque()
        stack.append([0, 0, 1])
        while stack:
            x, y, step = stack.popleft()
            if x == N - 1 and y == N - 1 and grid[x][y] == 0: return step
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]:
                if 0 <= dx + x < N and 0 <= dy + y < N and grid[dx + x][dy + y] == 0 and (
                        dx + x, dy + y) not in visit:
                    stack.append([dx + x, dy + y, step + 1])
                    visit.add((dx + x, dy + y))
        return -1


grid = [[0, 1], [1, 0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))
