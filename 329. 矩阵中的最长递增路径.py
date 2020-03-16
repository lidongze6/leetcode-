class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        res = 0
        self.ret = [[-1 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if self.ret[i][j] != -1:
                    res = max(res, self.ret[i][j])
                else:
                    res = max(res, self.dfs(i, j, matrix, r, c))
        return res

    def dfs(self, i, j, matrix, m, n):
        if self.ret[i][j] != -1:
            return self.ret[i][j]

        self.ret[i][j] = 1
        for d1, d2 in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            if 0 <= i + d1 < m and 0 <= j + d2 < n and matrix[i + d1][j + d2] > matrix[i][j]:
                self.ret[i][j] = max((1 + self.dfs(i + d1, j + d2, matrix, m, n)), self.ret[i][j])
        return self.ret[i][j]
