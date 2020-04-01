class Solution:
    def maxDistance(self, grid) -> int:
        from collections import deque
        if not grid: return 0
        N = len(grid)
        dis = [[-1] * N for i in range(N)]
        visit = set()
        stack = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    visit.add((i, j))
                    stack.append((i, j))
                    dis[i][j] = 0
        if len(visit) == 0 or len(visit) == N * N:
            return -1
        res = 0
        while stack:
            x, y = stack.popleft()
            for dx, dy in [[0, 1], [0, - 1], [1, 0], [- 1, 0]]:
                if 0 <=x+dx < N and 0 <= y+dy < N and (x+dx, y+dy) not in visit:
                    dis[x+dx][y+dy] = dis[x][y] + 1
                    visit.add((x+dx, y+dy))
                    stack.append((x+dx, y+dy))
                    res = max(res, dis[x+dx][y+dy])

        return res

grid=[[1,0,1],[0,0,0],[1,0,1]]
print(Solution().maxDistance(grid))