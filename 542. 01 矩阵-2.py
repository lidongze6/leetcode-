class Solution:
    def updateMatrix(self, matrix):
        # BFS 对每个0进行bfs，计算离每个0最近的1的距离
        from collections import deque
        m, n = len(matrix), len(matrix[0])
        stack = deque()
        visit = set()
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i, j))

        step = 0
        while stack:
            l = len(stack)
            for i in range(l):
                x, y = stack.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in visit:
                        visit.add((x + dx, y + dy))
                        stack.append((x + dx, y + dy))
            step += 1

        return res