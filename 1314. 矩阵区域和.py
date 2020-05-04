class Solution:
    def matrixBlockSum(self, mat, K: int):
        # 二维前缀和问题
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i][j - 1] + presum[i-1][j] - presum[i - 1][j - 1] + mat[i - 1][j - 1]

        res = [[0] * (n) for i in range(m)]

        for i in range(m):
            for j in range(n):
                x0 = max(0, i - K)
                x1 = min(i + K + 1, m)
                y0 = max(0, j - K)
                y1 = min(j + K + 1, n)
                res[i][j] = presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0]
        return res
