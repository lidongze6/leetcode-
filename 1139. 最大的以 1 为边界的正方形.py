class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        ud = [[0] * (n + 1) for i in range(m + 1)]
        lr = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m):
            for j in range(n):
                # ud[i][j] 表示 (i, j) 的上边有多少个 1
                ud[i + 1][j] = ud[i][j] + grid[i][j]
                # lr[i][j] 表示 (i, j) 的左边有多少个 1
                lr[i][j + 1] = lr[i][j] + grid[i][j]

        edges = [0, 0, 0, 0]
        for k in range(min(m, n), 0, -1):  # 逆序遍历，存在则直接返回的就是当前最大的
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    # 判断上边
                    edges[0] = ud[i + k][j] - ud[i][j]
                    # 判断下边
                    edges[1] = ud[i + k][j + k - 1] - ud[i][j + k - 1]
                    # 判断左边
                    edges[2] = lr[i][j + k] - lr[i][j]
                    # 判断右边
                    edges[3] = lr[i + k - 1][j + k] - lr[i + k - 1][j]
                    # 判断是否满足
                    if all([edge == k for edge in edges]):
                        return k * k
        return 0


grid = [[1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]
print(Solution().largest1BorderedSquare(grid))
