class Solution:
    def PredictTheWinner(self, piles: List[int]) -> bool:
        if len(piles) == 1: return True
        m = len(piles)
        f = [[[0, 0] for _ in range(m)] for _ in range(m)]
        for i in range(m):
            f[i][i][0] = piles[i]

        for k in range(1, m + 1):
            for i in range(m):
                j = i + k
                if j >= m:
                    break
                left = piles[i] + f[i + 1][j][1]
                right = piles[j] + f[i][j - 1][1]

                if left > right:
                    f[i][j][0] = left
                    f[i][j][1] = f[i + 1][j][0]
                else:
                    f[i][j][0] = right
                    f[i][j][1] = f[i][j - 1][0]

        res = f[0][m - 1]
        return (res[0] - res[1]) >= 0
