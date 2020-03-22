class Solution:
    def minimumTotal(self, triangle) -> int:
        # dfs+记忆化
        dic = dict()

        def dfs(x, y):
            if x == len(triangle) - 1:
                return triangle[x][y]
            elif (x, y) in dic:
                return dic[(x, y)]
            else:
                tmp = min(dfs(x + 1, y), dfs(x + 1, y + 1)) + triangle[x][y]
                dic[(x, y)] = tmp
                return tmp

        return dfs(0, 0)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))
