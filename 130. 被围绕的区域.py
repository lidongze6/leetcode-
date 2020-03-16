class Solution:
    def solve(self, board):
        if not board: return []
        r, c = len(board), len(board[0])
        self.visit = set()
        for i in range(r):
            self.dfs(i, 0, board, r, c)
            self.dfs(i, c - 1, board, r, c)

        for j in range(c):
            self.dfs(0, j, board, r, c)
            self.dfs(r - 1, j, board, r, c)


        return board

    def dfs(self, i, j, board, r, c):
        if (i, j) in self.visit:
            return
        self.visit.add((i, j))
        if board[i][j] == "O":
            board[i][j] = "#"
            for d1, d2 in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                tmp = (i + d1, j + d2)
                if 0 <= tmp[0] < r and 0 <= tmp[1] < c and tmp not in self.visit and board[tmp[0]][tmp[1]] == "O":
                    self.dfs(tmp[0], tmp[1], board, r, c)
        return


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
s = Solution()
print(s.solve(board))
