class Solution:
    def updateMatrix(self, matrix):
        if not matrix: return []
        r, c = len(matrix), len(matrix[0])
        self.res = [[0 for i in range(c)] for j in range(r)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] != 0:
                    self.res[i][j] = self.bfs(i, j, matrix, 0, r, c)
        return self.res

    def bfs(self, i, j, matrix, step, r, c):
        from collections import deque
        stack = deque()
        stack.append((i, j))
        visit = set()
        while stack:
            step += 1
            for _ in range(len(stack)):
                x, y = stack.popleft()
                visit.add((x, y))
                for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    tmp = (x + d1, y + d2)
                    if 0 <= tmp[0] < r and 0 <= tmp[1] < c and tmp not in visit:
                        if matrix[tmp[0]][tmp[1]] != 0:
                            stack.append(tmp)
                        else:
                            return step

matrix = [[0,0,0],[0,1,0],[0,0,0]]
s = Solution()
print(s.updateMatrix(matrix))
matrix1 = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
