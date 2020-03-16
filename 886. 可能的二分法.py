class Solution:
    def possibleBipartition(self, N, dislikes):
        from collections import defaultdict
        if N == 1: return True
        self.visit = set()
        self.start = [0] * (N + 1)
        connection = defaultdict(list)
        for first, second in dislikes:
            connection[first].append(second)
            connection[second].append(first)

        for i in range(1, N + 1):
            if i in self.visit:
                continue
            else:
                self.start[i] = 1
                if not self.dfs(i, connection):
                    return False
        return True

    def dfs(self, cur, connection):
        if cur in self.visit:
            return True
        self.visit.add(cur)
        for node in connection[cur]:
            if self.start[node] * self.start[cur] == 1:
                return False
            self.start[node] = self.start[cur] * -1
            if not self.dfs(node, connection):
                return False
        return True


N = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
s = Solution()
print(s.possibleBipartition(N, dislikes))
