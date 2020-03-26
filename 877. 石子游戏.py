class Solution:
    def stoneGame(self, piles):
        if len(piles) == 1: return True
        m = len(piles)
        f = [[[0, 0] for _ in range(m)] for _ in range(m)]
        # f[i][j] 表示piles[i:j+1],f[i][j][0]为先手所能得到的最大值,f[i][j][1]为后手所能得到的最大值
        # 所求为f[0][m-1][0]-f[0][m-1][1] 是否大于0
        for i in range(m):
            f[i][i][0] = piles[i]

        # 需要斜着遍历
        for k in range(1, m + 1):  # 表示横纵坐标之差
            for i in range(m):
                j = i + k
                if j >= m:
                    break

                # 从左边拿:
                left = piles[i] + f[i + 1][j][1]
                # 从右边拿:
                right = piles[j] + f[i][j - 1][1]

                if left > right:
                    f[i][j][0] = left
                    f[i][j][1] = f[i + 1][j][0]
                else:
                    f[i][j][0]=right
                    f[i][j][1]=f[i][j-1][0]

        res = f[0][m- 1]
        return res[0] - res[1]

print(Solution().stoneGame([1,5,2]))