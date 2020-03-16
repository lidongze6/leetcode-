class Solution:
    def loudAndRich(self, richer, quiet):
        from collections import defaultdict
        l = len(quiet)
        connetion = defaultdict(list)
        for x, y in richer:
            connetion[y].append(x)
        res = [-1] * l
        for i in range(l):
            if res[i] == -1:
                self.dfs(i, connetion, res, quiet)
        return res

    def dfs(self, cur, connection, res, quiet):
        if connection[cur]:
            for i in connection[cur]:
                if res[i] == -1:
                    self.dfs(i, connection, res, quiet)
                if quiet[cur] > quiet[i]:
                    quiet[cur] = quiet[i]
                    res[cur] = res[i]
            if res[cur] == -1:
                res[cur] = cur
        else:
            res[cur] = cur


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
s = Solution()
print(s.loudAndRich(richer, quiet))
