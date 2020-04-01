class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # 二维背包型DP ，但是超时
        l = len(strs)
        if l < 1: return 0

        f = [[[0] * (n + 1) for i in range(m + 1)] for j in range(l + 1)]
        # f[k][i][j] 前k个物品在消耗i个0 j个1后所能拼出的最大数量
        from collections import Counter
        dic=[Counter(x) for x in strs]

        for k in range(1, l + 1):
            for i in range(0, m + 1):
                for j in range(0, n + 1):
                    f[k][i][j] = f[k - 1][i][j]
                    if j - dic[k - 1]["1"] >= 0 and i - dic[k - 1]["0"] >= 0:
                        f[k][i][j] = max(f[k][i][j], f[k-1][i - dic[k - 1]["0"]][j - dic[k - 1]["1"]] + 1)
        return f[l][m][n]


Array = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(Array, m, n))
