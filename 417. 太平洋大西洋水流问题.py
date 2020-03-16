class Solution:
    def pacificAtlantic(self, matrix):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.Pa = set()
        self.At = set()
        for i in range(self.row):
            self.dfs_Pa(i, 0, matrix)
            self.dfs_At(i, self.col - 1, matrix)

        for j in range(self.col):
            self.dfs_At(self.row - 1, j, matrix)
            self.dfs_Pa(0, j, matrix)

        res = list(self.Pa.intersection(self.At))
        return [list(i) for i in res]

    def dfs_Pa(self, ri, ci, matrix):
        from collections import deque
        stack = deque()
        stack.append([ri, ci])
        while stack:
            r, c = stack.popleft()
            self.Pa.add((r, c))
            dire = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for d in dire:
                tmp = [r + d[0], c + d[1]]
                if tuple(tmp) not in self.Pa and 0 <= tmp[0] < self.row and 0 <= tmp[1] < self.col and matrix[tmp[0]][
                    tmp[1]] >= matrix[r][c]:
                    stack.append(tmp)

    def dfs_At(self, ri, ci, matrix):
        from collections import deque
        stack = deque()
        stack.append([ri, ci])
        while stack:
            r, c = stack.popleft()
            self.At.add((r, c))
            dire = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for d in dire:
                tmp = [r + d[0], c + d[1]]
                if tuple(tmp) not in self.At and 0 <= tmp[0] < self.row and 0 <= tmp[1] < self.col and matrix[tmp[0]][
                    tmp[1]] >= matrix[r][c]:
                    stack.append(tmp)


matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

s = Solution()
print(s.pacificAtlantic(matrix))
