class Solution:
    def gameOfLife(self, board) -> None:
        m, n = len(board), len(board[0])

        # 0：从始至终死了的
        # 1：从始至终活着的
        # 2：活--->死
        # 3：死--->活

        for i in range(m):
            for j in range(n):
                tmp = 0
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        if board[i + dx][j + dy] in [1, 2]:
                            tmp += 1
                if board[i][j] == 1:  # 活着的
                    if tmp not in [2, 3]:
                        board[i][j] = 2
                if board[i][j] == 0:  # 死了的
                    if tmp == 3:
                        board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]
Solution().gameOfLife(board)
print(board)
