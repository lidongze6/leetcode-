class Solution:
    def numRookCaptures(self, board) -> int:
        res = 0

        def dfs(x, y, dx, dy):
            nonlocal res
            if board[x][y] == "p":
                res += 1
                return
            elif board[x][y] == "B":
                return
            elif 0 <= x+dx < 8 and 0 <= y+dy < 8:
                dfs(x + dx, y + dy, dx, dy)

        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    dfs(i, j, 1, 0)
                    dfs(i, j, -1, 0)
                    dfs(i, j, 0, 1)
                    dfs(i, j, 0, -1)
                    return res


board=[[".",".",".",".",".",".",".","."],
       [".",".",".","p",".",".",".","."],
       [".",".",".","R",".",".",".","p"],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".","p",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."]]
print(Solution().numRookCaptures(board))