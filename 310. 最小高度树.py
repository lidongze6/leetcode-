class Solution:
    def findMinHeightTrees(self, n, edges):
        # bfs 超时
        from collections import defaultdict
        from collections import deque
        connections = defaultdict(list)
        for x, y in edges:
            connections[x].append(y)
            connections[y].append(x)

        def bfs(i):
            visit = set()
            stack = deque()
            stack.append([i, 1])
            while stack:
                cur, level = stack.popleft()
                visit.add(cur)
                for node in connections[cur]:
                    if node not in visit:
                        stack.append([node, level + 1])
            return level, i

        res = n
        tmp = []
        for i in range(n):
            l, no = bfs(i)
            if res > l:
                res = l
                tmp = [no]
            elif res == l:
                tmp.append(no)
        return tmp


n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
s = Solution()
print(s.findMinHeightTrees(n, edges))
