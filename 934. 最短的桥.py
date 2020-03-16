class Solution:
    def shortestBridge(self, A):
        from collections import deque
        row = len(A)
        col = len(A[0])
        stack = deque()
        flag = False
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    self.dfs(i, j, A, row, col, stack)
                    flag = True
                    break
            if flag:
                break

        while stack:
            x, y, step = stack.popleft()
            if A[x][y] == 1: return step
            for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + d1 < row and 0 <= y + d2 < col and A[x + d1][y + d2] != 2:
                    stack.append([x + d1, y + d2, step + 1])

    def dfs(self, x, y, A, row, col, stack):
        A[x][y] = 2
        stack.append([x, y, -1])
        for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= x + d1 < row and 0 <= y + d2 < col and A[x + d1][y + d2] == 1:
                self.dfs(x + d1, y + d2, A, row, col, stack)
        return


A =[[0,1],[1,0]]
s = Solution()
print(s.shortestBridge(A))
