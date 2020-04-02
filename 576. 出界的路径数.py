class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # dfs+记忆化
        import collections
        MOD = 10 ** 9 + 7
        dic = collections.defaultdict(int)

        def dfs(x, y, step):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            elif step == 0:
                return 0
            elif (x, y, step) in dic:
                return dic[(x, y, step)]
            else:
                res = 0
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    res += dfs(x + dx, y + dy, step - 1)
                    dic[(x, y, step)] = res
                return res

        return dfs(i, j, N) % MOD

m = 2
n = 2
N = 2
i = 0
j = 0
print(Solution().findPaths(m,n,N,i,j))