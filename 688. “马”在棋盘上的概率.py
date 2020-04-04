class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int):
        dic = dict()

        def dfs(x, y, c):
            if x < 0 or x >= N or y < 0 or y >= N:
                return 0
            if c == 0:
                return 1
            if (x, y, c) in dic:
                return dic[(x, y, c)]
            else:
                res = 0
                for dx, dy in [[-1, -2], [-1, 2], [1, -2], [1, 2], [-2, -1], [-2, 1], [2, -1], [2, 1]]:
                    res += dfs(x + dx, y + dy, c - 1)
                dic[(x, y, c)] = res/8
                return res/8


        return dfs(r, c, K)


N, K, r, c = 3, 2, 0, 0
print(Solution().knightProbability(N, K, r, c))
