class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        # 坐标型DP
        res=0
        m, n = len(matrix), len(matrix[0])  # 记录以(i,j)为右下角点的最大正方形大小
        f = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:  # 边界且值为1 则最大只能为1
                        f[i][j] = 1
                    else:
                        f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                res = max(res, f[i][j])
        return res * res


martrix = [["0", "0", "0", "1"],
           ["1", "1", "0", "1"],
           ["1", "1", "1", "1"],
           ["0", "1", "1", "1"],
           ["0", "1", "1", "1"]]
print(Solution().maximalSquare(martrix))
