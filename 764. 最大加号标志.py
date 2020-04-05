class Solution:
    def orderOfLargestPlusSign(self, N: int, mines) -> int:
        matrix = [[N] * N for i in range(N)]
        for x, y in mines:
            matrix[x][y] = 0

        for i in range(N):
            left, right = 0, 0
            for j in range(N):
                if matrix[i][j] != 0:
                    left += 1
                else:
                    left = 0
                matrix[i][j] = min(matrix[i][j], left)

            for j in range(N - 1, -1, -1):
                if matrix[i][j] != 0:
                    right += 1
                else:
                    right = 0
                matrix[i][j] = min(matrix[i][j], right)

        for i in range(N):
            up, down = 0, 0
            for j in range(N):
                if matrix[j][i] != 0:
                    up += 1
                else:
                    up = 0
                matrix[j][i] = min(matrix[j][i], up)

            for j in range(N - 1, -1, -1):
                if matrix[j][i] != 0:
                    down += 1
                else:
                    down = 0
                matrix[j][i] = min(matrix[j][i], down)

        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, matrix[i][j])
        return res

N=10
mines=[[0,0],[0,3],[0,7],[1,1],[1,2],[1,8],[1,9],[2,0],[2,5],[2,6],[2,9],[3,2],[3,4],[3,7],[4,0],[4,3],[4,6],[4,7],[5,0],[5,8],[5,9],[6,2],[6,3],[6,8],[6,9],[7,0],[7,1],[7,5],[7,9],[8,4],[8,9],[9,1],[9,3],[9,4],[9,8],[9,9]]