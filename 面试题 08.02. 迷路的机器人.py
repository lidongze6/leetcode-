class Solution:
    def pathWithObstacles(self, obstacleGrid):
        # DFS 回溯
        if not obstacleGrid or obstacleGrid[0][0] == 1: return []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        visit = set()
        res = []

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                res.append([x, y])
                return True
            res.append([x, y])
            flag = False
            for dx, dy in [[0, 1], [1, 0]]:
                if x + dx < m and y + dy < n and obstacleGrid[x + dx][y + dy] != 1 and (x + dx, y + dy) not in visit:
                    visit.add((x + dx, y + dy))
                    flag |= dfs(x + dx, y + dy)
            if flag:
                return True
            else:
                res.pop()
            return False

        dfs(0, 0)
        return res


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().pathWithObstacles(obstacleGrid))
