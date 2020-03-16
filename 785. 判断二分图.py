class Solution:
    def isBipartite(self, graph):
        self.start = [0 for _ in range(len(graph))]
        self.seen = set()
        for i in range(len(self.start)):
            if i in self.seen:
                continue
            else:
                self.start[i] = 1
                if not self.dfs(i, graph):
                    return False
        return True

    def dfs(self, cur, graph):
        if cur in self.seen:
            return True
        else:
            self.seen.add(cur)
        for j in graph[cur]:
            if self.start[j] * self.start[cur] == 1:
                return False
            self.start[j] = self.start[cur] * -1
            if not self.dfs(j, graph):
                return False
        return True


s = Solution()
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
