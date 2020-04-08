class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 1
        visit = set()
        visit.add((0,0))

        def dfs(x, y):
            nonlocal res
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in visit and helper(x + dx) + helper(
                        y + dy) <= k:
                    visit.add((x + dx, y + dy))
                    res += 1
                    dfs(x + dx, y + dy)

            return

        def helper(x):
            sum = 0
            while x >= 10:
                div, mod = divmod(x, 10)
                sum += mod
                x = div
            return sum + x

        dfs(0, 0)
        return res


m = 1
n = 2
k = 1
print(Solution().movingCount(m,n,k))